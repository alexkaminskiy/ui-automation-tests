from pages.base_page import BasePage
from playwright.sync_api import Page


class EmployeesPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.add_button = page.get_by_role("link", name="+ New Employee")
        self.table_rows = "table tbody tr"

    def open_add_employee(self):
        self.add_button.click()

    def get_employee_list(self):
        employee_list = self.page.locator(self.table_rows).all_inner_texts()
        print(employee_list)
        
        return employee_list