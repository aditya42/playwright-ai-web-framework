import pytest
from config.config import settings
from tests.pages.login_page import LoginPage
from src.ai_agents.self_healing_locator_agent import SelfHealingLocatorAgent

@pytest.mark.ai
@pytest.mark.smoke
def test_ai_agent_finds_login_button_with_fallback(page):
    login_page = LoginPage(page)
    agent = SelfHealingLocatorAgent()

    login_page.open()
    login_page.fill(login_page.USERNAME, settings.username)
    login_page.fill(login_page.PASSWORD, settings.password)

    login_button = agent.run(
        page,
        primary_selector="#non-existing-login-button",
        fallback_selectors=["#login-button", "input[type='submit']"]
    )
    login_button.click()

    page.locator(".title").wait_for()
    assert page.locator(".title").inner_text() == "Products"
