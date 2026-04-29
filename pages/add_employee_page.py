from pages.base_page import BasePage
from playwright.sync_api import Page


class AddEmployeePage(BasePage):

    url = None  # Form only accessible via navigation from EmployeesPage

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.name_input = self.page.get_by_role("textbox", name="Full Name")
        self.age_input = self.page.get_by_role("spinbutton", name="Age")
        self.salary_input = self.page.get_by_role("spinbutton", name="Monthly Salary")
        self.duration_input = self.page.get_by_role("spinbutton", name="Duration Worked (months)")
        self.grade_input = self.page.get_by_label("Grade")
        self.email_input = self.page.get_by_role("textbox", name="Email Address")
        self.save_btn = self.page.get_by_role("button", name="✓ Create Employee")

    def add_employee(
        self, name: str, age: int, salary: int, duration: int, grade: int, email: str
    ) -> None:
        """
        Fill and submit the add employee form.

        Args:
            name: Full name of the employee (e.g., "John Doe")
            age: Age of the employee in years
            salary: Monthly salary in currency units
            duration: Duration worked in months
            grade: Employee grade/level (integer representation of grade number)
            email: Email address of the employee

        Raises:
            AssertionError: If form fields are not visible or form submission fails
        """
        # self.page.screencast.start(path="reports/videos/vide0_debug.webm")
        self.name_input.fill(name)
        self.age_input.fill(str(age))
        self.salary_input.fill(str(salary))
        self.duration_input.fill(str(duration))
        self.grade_input.select_option(str(grade))
        self.email_input.fill(email)
        self.save_btn.click()
        # self.page.screencast.stop()