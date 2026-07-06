from src.ai_agents.base_agent import BaseAgent

class DefectSummaryAgent(BaseAgent):
    name = "defect-summary-agent"

    def run(self, test_name: str, error: str, page_url: str | None = None) -> str:
        return (
            f"Potential defect detected in {test_name}. "
            f"URL: {page_url or 'not captured'}. "
            f"Observed failure: {error}. "
            "Recommended triage: verify locator changes, environment stability, test data, and product behavior."
        )
