import pytest
from config.config import settings
from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage
from tests.pages.cart_page import CartPage

@pytest.mark.regression
def test_user_can_add_product_to_cart(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login(settings.username, settings.password)
    products_page.assert_loaded()

    products_page.add_first_product_to_cart()
    products_page.assert_cart_count("1")
    products_page.click(products_page.CART_LINK)

    cart_page.assert_loaded()
    cart_page.assert_item_present()
