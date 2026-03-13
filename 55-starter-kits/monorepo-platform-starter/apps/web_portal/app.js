async function fetchJson(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Request failed: ${path}`);
  }
  return response.json();
}

async function main() {
  try {
    const summary = await fetchJson("/api/summary");
    document.getElementById("summary-root").textContent =
      `${summary.total_items} items, ${summary.high_risk_count} high risk`;
  } catch (error) {
    document.getElementById("summary-root").textContent = "Failed to load summary.";
    console.error(error);
  }
}

main();
