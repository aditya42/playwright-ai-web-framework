from src.ai_agents.base_agent import BaseAgent

class TestCaseGeneratorAgent(BaseAgent):
    name = "test-case-generator-agent"

    def run(self, feature: str, acceptance_criteria: list[str]) -> list[str]:
        scenarios = []
        for index, criterion in enumerate(acceptance_criteria, start=1):
            scenarios.append(f"TC{index}: Validate that {feature} satisfies: {criterion}")
        return scenarios
