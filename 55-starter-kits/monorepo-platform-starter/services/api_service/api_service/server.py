from __future__ import annotations

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path

from .service import build_summary, load_items

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_DATA_PATH = ROOT / "examples" / "items.json"
DEFAULT_STATIC_ROOT = ROOT / "apps" / "web_portal"


def _make_handler(data_path: Path, static_root: Path) -> type[BaseHTTPRequestHandler]:
    class StarterHandler(BaseHTTPRequestHandler):
        def _send_json(self, status: HTTPStatus, payload: dict[str, object]) -> None:
            body = json.dumps(payload, sort_keys=True).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _send_bytes(self, status: HTTPStatus, body: bytes, content_type: str) -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _serve_static(self, relative: str, content_type: str) -> None:
            path = static_root / relative
            if not path.exists():
                self._send_bytes(HTTPStatus.NOT_FOUND, b"Not found.", "text/plain; charset=utf-8")
                return
            self._send_bytes(HTTPStatus.OK, path.read_bytes(), content_type)

        def do_GET(self) -> None:  # noqa: N802
            if self.path == "/":
                self._serve_static("index.html", "text/html; charset=utf-8")
                return
            if self.path == "/static/app.js":
                self._serve_static("app.js", "application/javascript; charset=utf-8")
                return
            if self.path == "/static/styles.css":
                self._serve_static("styles.css", "text/css; charset=utf-8")
                return
            if self.path == "/api/items":
                items = [item.to_dict() for item in load_items(data_path)]
                self._send_json(HTTPStatus.OK, {"items": items})
                return
            if self.path == "/api/summary":
                summary = build_summary(load_items(data_path)).to_dict()
                self._send_json(HTTPStatus.OK, summary)
                return
            self._send_bytes(HTTPStatus.NOT_FOUND, b"Not found.", "text/plain; charset=utf-8")

        def log_message(self, format: str, *args: object) -> None:
            return

    return StarterHandler


def make_server(host: str = "127.0.0.1", port: int = 8000, *, data_path: Path = DEFAULT_DATA_PATH, static_root: Path = DEFAULT_STATIC_ROOT) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), _make_handler(data_path, static_root))


def run_server(host: str = "127.0.0.1", port: int = 8000, *, data_path: Path = DEFAULT_DATA_PATH, static_root: Path = DEFAULT_STATIC_ROOT) -> None:
    server = make_server(host=host, port=port, data_path=data_path, static_root=static_root)
    print(f"Serving starter platform on http://{host}:{server.server_port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
