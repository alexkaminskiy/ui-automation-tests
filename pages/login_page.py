from pages.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):

    url = "/Account/Login"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.get_by_role("textbox", name="User Name")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Sign In")

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()