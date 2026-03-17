from pages.base_page import BasePage
from playwright.sync_api import Page


class AddEmployeePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.name_input = page.get_by_role("textbox", name="Full Name")
        self.age_input = page.get_by_role("spinbutton", name="Age")
        self.salary_input = page.get_by_role("spinbutton", name="Monthly Salary")
        self.duration_input = page.get_by_role("spinbutton", name="Duration Worked (months)")
        self.grade_input = page.get_by_label("Grade")
        self.email_input = page.get_by_role("textbox", name="Email Address")
        self.save_btn = page.get_by_role("button", name="✓ Create Employee")

    def add_employee(self, name, age, salary, duration, grade, email):
        self.name_input.fill(name)
        self.age_input.fill(str(age))
        self.salary_input.fill(str(salary))
        self.duration_input.fill(str(duration))
        self.grade_input.select_option(str(grade))
        self.email_input.fill(email)
        self.save_btn.click()