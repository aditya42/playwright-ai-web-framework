from tests.pages.base_page import BasePage
from config.config import settings

class LoginPage(BasePage):
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR = "[data-test='error']"

    def open(self):
        self.navigate(settings.base_url)

    def login(self, username: str, password: str):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
