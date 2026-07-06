from playwright.sync_api import sync_playwright, Browser, Page
from config.config import settings

class BrowserManager:
    def __init__(self):
        self.playwright = None
        self.browser: Browser | None = None
        self.page: Page | None = None

    def start(self) -> Page:
        self.playwright = sync_playwright().start()
        browser_type = getattr(self.playwright, settings.browser)
        launch_options = {"headless": settings.headless, "slow_mo": settings.slow_mo}
        if settings.chromium_executable_path and settings.browser == "chromium":
            launch_options["executable_path"] = settings.chromium_executable_path
        self.browser = browser_type.launch(**launch_options)
        context = self.browser.new_context(viewport={"width": 1440, "height": 900})
        context.set_default_timeout(settings.timeout)
        self.page = context.new_page()
        return self.page

    def stop(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
