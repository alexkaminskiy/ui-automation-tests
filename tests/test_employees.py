import allure
from utils.helpers import get_user_credentials
import pytest
from pages.employees_page import EmployeesPage
from pages.add_employee_page import AddEmployeePage


EMPLOYEE_NAME = "Alex Smith"
EMPLOYEE_AGE = 20
EMPLOYEE_SALARY = 120000
EMPLOYEE_DURATION = 24
EMPLOYEE_GRADE = 3
EMPLOYEE_EMAIL = "alex@smith.com"


@pytest.mark.ui
@allure.title("Add and delete a new employee")
@allure.description("Test adding a new employee to the system and then verifying deletion")
@allure.feature("Employee Management")
@allure.story("Add Employee")
def test_add_new_employee(app):
    with allure.step("Login to the application"):
        username, password = get_user_credentials("admin")
        home = app.login(username, password)
    
    with allure.step("Navigate to employees page"):
        home.go_to_employees()

    with allure.step("Open add employee form"):
        emp_page = EmployeesPage(app.page)
        emp_page.open_add_employee()

    with allure.step(f"Add new employee: {EMPLOYEE_NAME}"):
        add_page = AddEmployeePage(app.page)
        add_page.add_employee(
                name=EMPLOYEE_NAME,
                age=EMPLOYEE_AGE,
                salary=EMPLOYEE_SALARY,
                duration=EMPLOYEE_DURATION,
                grade=EMPLOYEE_GRADE,
                email=EMPLOYEE_EMAIL,
        )

    with allure.step("Verify employee was added to the list"):
        employees = emp_page.get_employee_list()
        assert any(EMPLOYEE_NAME in row for row in employees), (
            f"Employee '{EMPLOYEE_NAME}' was not found in the list after adding"
        )
    
    with allure.step(f"Delete employee: {EMPLOYEE_NAME}"):
        emp_page.delete_employee(EMPLOYEE_NAME)
    
    with allure.step("Verify employee was deleted from the list"):
        employees = emp_page.get_employee_list()
        assert not any(EMPLOYEE_NAME in row for row in employees), (
            f"Employee '{EMPLOYEE_NAME}' was still found in the list after deletion"
        )


@pytest.mark.skip(reason="Temp disabled")
@allure.title("Delete employee Alex Smith")
@allure.description("Test deleting an employee (Alex Smith) from the employees list")
@allure.feature("Employee Management")
@allure.story("Delete Employee")
def test_delete_employee(app):
    """Test deleting an employee (Alex Smith) from the employees list."""
    with allure.step("Login to the application"):
        username, password = get_user_credentials("admin")
        home = app.login(username, password)
    
    with allure.step("Navigate to Employees page"):
        app.page.click("a:has-text(\"Employees\")")
        app.page.wait_for_load_state("networkidle")
    
    with allure.step("Get employee list before deletion"):
        employees_page = EmployeesPage(app.page)
        employee_list_before = employees_page.get_employee_list()
        alex_count_before = sum(1 for emp in employee_list_before if "Alex Smith" in emp)
        allure.attach(f"Alex Smith count before deletion: {alex_count_before}", name="Pre-deletion count", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Delete Alex Smith"):
        employees_page.delete_employee("Alex Smith")
    
    with allure.step("Get employee list after deletion"):
        employee_list_after = employees_page.get_employee_list()
        alex_count_after = sum(1 for emp in employee_list_after if "Alex Smith" in emp)
        allure.attach(f"Alex Smith count after deletion: {alex_count_after}", name="Post-deletion count", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Verify deletion was successful"):
        assert alex_count_after == 0, f"Alex Smith should be deleted, but found {alex_count_after} instances"
        assert alex_count_before > 0, "Alex Smith should have existed before deletion"