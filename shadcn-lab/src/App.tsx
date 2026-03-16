import {
  Point93DashboardPage,
  type DashboardScenario,
} from "@/components/dashboard/dashboard-page"

function getDashboardScenario(): DashboardScenario {
  const raw = new URLSearchParams(window.location.search).get("scenario")

  if (raw === "partial" || raw === "active" || raw === "zero") {
    return raw
  }

  return "zero"
}

export function App() {
  return <Point93DashboardPage scenario={getDashboardScenario()} />
}

export default App
