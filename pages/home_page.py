from pages.base_page import BasePage
from playwright.sync_api import Page
from utils.waits import wait_visible


class HomePage(BasePage):
    
    url = "/Employee"

    def __init__(self, page: Page):
        super().__init__(page)

        self.employees_link = self.page.get_by_role("link", name="👥 Employees")
        self.home_link = self.page.get_by_role("link", name="🏠 Home")
        self.logout_link = self.page.get_by_role("button", name="Logout")
        self.heading_message = self.page.get_by_role("heading", name="Employee Management Built for")

    def get_heading_message(self) -> str:
        """Retrieve the main heading message from the home page.

        Returns:
            str: The text content of the heading message
        """
        return self.heading_message.inner_text()
    
    def go_to_employees(self) -> None:
        """Navigate to the employees page."""
        self.open()

    def go_to_home_page(self) -> None:
        """Navigate back to the home page."""
        self.home_link.click()

    def logout(self) -> None:
        """Log out the current user."""
        self.logout_link.click()