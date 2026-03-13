async function fetchJson(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Request failed: ${path}`);
  }
  return response.json();
}

function updateSummary(summary) {
  document.getElementById("total-items").textContent = String(summary.total_items);
  document.getElementById("high-risk-count").textContent = String(summary.high_risk_count);
  document.getElementById("blocked-count").textContent = String(summary.blocked_items.length);
  document.getElementById("runbook-gap-count").textContent = String(summary.runbook_gaps.length);
}

function renderItems(items) {
  const root = document.getElementById("items-root");
  root.innerHTML = "";

  for (const item of items) {
    const card = document.createElement("article");
    card.className = "item-card";
    card.innerHTML = `
      <h3>${item.id}: ${item.title}</h3>
      <p>${item.owner} owns ${item.area}.</p>
      <div class="meta-row">
        <span class="chip status-${item.status}">${item.status}</span>
        <span class="chip">risk: ${item.risk_level}</span>
        <span class="chip">target: ${item.deployment_target}</span>
        <span class="chip">runbook: ${item.has_runbook ? "yes" : "no"}</span>
      </div>
    `;
    root.appendChild(card);
  }
}

async function main() {
  try {
    const [summary, payload] = await Promise.all([
      fetchJson("/api/summary"),
      fetchJson("/api/work-items"),
    ]);
    updateSummary(summary);
    renderItems(payload.items);
  } catch (error) {
    const root = document.getElementById("items-root");
    root.innerHTML = `<p>Dashboard failed to load.</p>`;
    console.error(error);
  }
}

main();
