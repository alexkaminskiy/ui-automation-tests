from pages.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):

    url = "/Account/Login"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username = self.page.get_by_role("textbox", name="User Name")
        self.password = self.page.get_by_role("textbox", name="Password")
        self.login_button = self.page.get_by_role("button", name="Sign In")

    def login(self, user: str, pwd: str) -> None:
        """Log in with the provided credentials.

        Args:
            user: The username to authenticate with
            pwd: The password to authenticate with
        """
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()