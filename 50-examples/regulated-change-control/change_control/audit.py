from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3

from .models import AuditEvent, ControlPacket


def _normalize_payload(packet: ControlPacket) -> str:
    return json.dumps(packet.to_dict(), separators=(",", ":"), sort_keys=True)


def _hash_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _ensure_schema(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS audit_events (
            event_index INTEGER PRIMARY KEY,
            recorded_at TEXT NOT NULL,
            actor TEXT NOT NULL,
            action TEXT NOT NULL,
            system TEXT NOT NULL,
            payload_hash TEXT NOT NULL,
            previous_hash TEXT NOT NULL,
            chain_hash TEXT NOT NULL
        )
        """
    )
    connection.commit()


def append_audit_event(db_path: str | Path, actor: str, action: str, packet: ControlPacket) -> AuditEvent:
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(path)
    try:
        _ensure_schema(connection)
        last_row = connection.execute(
            """
            SELECT event_index, chain_hash
            FROM audit_events
            ORDER BY event_index DESC
            LIMIT 1
            """
        ).fetchone()

        event_index = 1 if last_row is None else int(last_row[0]) + 1
        previous_hash = "ROOT" if last_row is None else str(last_row[1])
        recorded_at = datetime.now(timezone.utc).isoformat()
        payload_hash = _hash_text(_normalize_payload(packet))
        chain_hash = _hash_text(
            "|".join(
                (
                    str(event_index),
                    recorded_at,
                    actor,
                    action,
                    packet.system,
                    payload_hash,
                    previous_hash,
                )
            )
        )

        connection.execute(
            """
            INSERT INTO audit_events (
                event_index,
                recorded_at,
                actor,
                action,
                system,
                payload_hash,
                previous_hash,
                chain_hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event_index,
                recorded_at,
                actor,
                action,
                packet.system,
                payload_hash,
                previous_hash,
                chain_hash,
            ),
        )
        connection.commit()

        return AuditEvent(
            event_index=event_index,
            recorded_at=recorded_at,
            actor=actor,
            action=action,
            system=packet.system,
            payload_hash=payload_hash,
            previous_hash=previous_hash,
            chain_hash=chain_hash,
        )
    finally:
        connection.close()


def verify_audit_chain(db_path: str | Path) -> tuple[bool, int]:
    path = Path(db_path)
    if not path.exists():
        return True, 0

    connection = sqlite3.connect(path)
    try:
        _ensure_schema(connection)
        rows = connection.execute(
            """
            SELECT event_index, recorded_at, actor, action, system, payload_hash, previous_hash, chain_hash
            FROM audit_events
            ORDER BY event_index ASC
            """
        ).fetchall()
    finally:
        connection.close()

    expected_previous_hash = "ROOT"
    for row in rows:
        event_index, recorded_at, actor, action, system, payload_hash, previous_hash, chain_hash = row
        expected_chain_hash = _hash_text(
            "|".join(
                (
                    str(event_index),
                    str(recorded_at),
                    str(actor),
                    str(action),
                    str(system),
                    str(payload_hash),
                    expected_previous_hash,
                )
            )
        )
        if previous_hash != expected_previous_hash or chain_hash != expected_chain_hash:
            return False, len(rows)
        expected_previous_hash = str(chain_hash)

    return True, len(rows)
