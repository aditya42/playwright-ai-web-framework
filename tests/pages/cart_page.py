from playwright.sync_api import expect
from tests.pages.base_page import BasePage

class CartPage(BasePage):
    CART_TITLE = ".title"
    CART_ITEM = ".cart_item"

    def assert_loaded(self):
        expect(self.page.locator(self.CART_TITLE)).to_have_text("Your Cart")

    def assert_item_present(self):
        expect(self.page.locator(self.CART_ITEM)).to_be_visible()
