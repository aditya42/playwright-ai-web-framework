import pytest
from playwright.sync_api import expect
from config.config import settings
from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage

@pytest.mark.smoke
def test_valid_user_can_login(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.open()
    login_page.login(settings.username, settings.password)

    products_page.assert_loaded()

@pytest.mark.regression
def test_invalid_user_gets_error(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("invalid_user", "wrong_password")

    expect(page.locator(login_page.ERROR)).to_be_visible()
    expect(page.locator(login_page.ERROR)).to_contain_text("Username and password do not match")
