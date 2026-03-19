from pages.base_page import BasePage
from playwright.sync_api import Page



class HomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.employees_link = page.get_by_role("link", name="👥 Employees")
        self.logout_link = page.get_by_role("button", name="Logout")
        self.heading_message = page.get_by_role("heading", name="Employee Management Built for")

    def get_heading_message(self):
        return self.heading_message.inner_text()
    
    def go_to_employees(self):
        self.employees_link.click()

    def logout(self):
        self.logout_link.click()