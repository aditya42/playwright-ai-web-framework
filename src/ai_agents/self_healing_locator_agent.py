from playwright.sync_api import Page
from src.ai_agents.base_agent import BaseAgent

class SelfHealingLocatorAgent(BaseAgent):
    name = "self-healing-locator-agent"

    def run(self, page: Page, primary_selector: str, fallback_selectors: list[str]):
        selectors = [primary_selector, *fallback_selectors]
        for selector in selectors:
            locator = page.locator(selector)
            try:
                if locator.count() > 0 and locator.first.is_visible(timeout=1500):
                    return locator.first
            except Exception:
                continue
        raise AssertionError(f"No working locator found. Tried: {selectors}")
