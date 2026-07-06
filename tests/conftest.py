import pytest
from src.core.browser_manager import BrowserManager

@pytest.fixture(scope="function")
def page():
    manager = BrowserManager()
    page = manager.start()
    yield page
    manager.stop()
