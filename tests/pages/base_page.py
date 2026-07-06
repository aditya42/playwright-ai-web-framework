from pathlib import Path
from urllib.parse import urlparse, unquote
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        if url.startswith("file://"):
            parsed_path = unquote(urlparse(url).path)
            html = Path(parsed_path).read_text(encoding="utf-8")
            self.page.set_content(html, wait_until="domcontentloaded")
            return
        self.page.goto(url, wait_until="domcontentloaded")

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str):
        self.page.locator(selector).fill(value)

    def assert_visible(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible()

    def text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()
