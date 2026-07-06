from playwright.sync_api import expect
from tests.pages.base_page import BasePage

class ProductsPage(BasePage):
    TITLE = ".title"
    INVENTORY_ITEMS = ".inventory_item"
    FIRST_ADD_TO_CART = "button[data-test^='add-to-cart']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    def assert_loaded(self):
        expect(self.page.locator(self.TITLE)).to_have_text("Products")
        expect(self.page.locator(self.INVENTORY_ITEMS).first).to_be_visible()

    def add_first_product_to_cart(self):
        self.page.locator(self.FIRST_ADD_TO_CART).first.click()

    def assert_cart_count(self, count: str):
        expect(self.page.locator(self.CART_BADGE)).to_have_text(count)
