from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from utils.waits import wait_visible
from typing import List


class EmployeesPage(BasePage):

    url = "/Employee"

    def __init__(self, page: Page):
        super().__init__(page)
        self.add_button = self.page.get_by_role("link", name="+ New Employee")
        self.table_rows = "xpath=//tbody"

    def open_add_employee(self) -> None:
        """Click the button to open the add employee form."""
        self.add_button.click()

    def get_employee_list(self) -> List[str]:
        """Retrieve the list of employees from the table.

        Returns:
            List[str]: A list of text content from each row in the employees table
        """
        wait_visible(self.page.locator(self.table_rows))
        employee_list = self.page.locator(self.table_rows).all_inner_texts()
        
        return employee_list

    def delete_employee(self, employee_name: str) -> None:
        """Delete an employee by name from the employees list.
        
        Args:
            employee_name: The name of the employee to delete (e.g., "Alex Smith")

        Raises:
            ValueError: If the employee is not found in the list
        """
        # Find the row containing the employee name
        rows = self.page.locator("tbody tr")
        employee_found = False
        
        for i in range(rows.count()):
            row_text = rows.nth(i).inner_text()
            if employee_name in row_text:
                employee_found = True
                # Click the delete button (🗑 Delete link with class btn-del)
                delete_link = rows.nth(i).locator("a.btn-del")
                delete_link.click()
                
                # Wait for delete confirmation page to load
                self.page.wait_for_load_state("domcontentloaded")
                
                # Click the Delete button to confirm deletion
                delete_button = self.page.get_by_role("button", name="Delete")
                expect(delete_button).to_be_visible()
                delete_button.click()
                
                # Wait for page to redirect back to employees list
                self.page.wait_for_load_state("networkidle")
                break
        
        if not employee_found:
            raise ValueError(f"Employee '{employee_name}' not found in the employees list")