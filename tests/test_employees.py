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


@pytest.mark.smoke
def test_add_new_employee(app):
    username, password = get_user_credentials("admin")
    home = app.login(username, password)
    home.go_to_employees()

    emp_page = EmployeesPage(app.page)
    emp_page.open_add_employee()

    add_page = AddEmployeePage(app.page)
    add_page.add_employee(
            name=EMPLOYEE_NAME,
            age=EMPLOYEE_AGE,
            salary=EMPLOYEE_SALARY,
            duration=EMPLOYEE_DURATION,
            grade=EMPLOYEE_GRADE,
            email=EMPLOYEE_EMAIL,
    )

    employees = emp_page.get_employee_list()
    assert any(EMPLOYEE_NAME in row for row in employees), (
        f"Employee '{EMPLOYEE_NAME}' was not found in the list after adding"
    )
    
    emp_page.delete_employee(EMPLOYEE_NAME)
    employees = emp_page.get_employee_list()
    assert not any(EMPLOYEE_NAME in row for row in employees), (
        f"Employee '{EMPLOYEE_NAME}' was still found in the list after deletion"
    )


@pytest.mark.skip(reason="Temp disabled")
def test_delete_employee_alex_smith(app):
    """Test deleting an employee (Alex Smith) from the employees list."""
    # Login and navigate to employees page
    username, password = get_user_credentials("admin")
    home = app.login(username, password)
    
    # Navigate to Employees page
    app.page.click("a:has-text(\"Employees\")")
    app.page.wait_for_load_state("networkidle")
    
    # Create EmployeesPage instance
    employees_page = EmployeesPage(app.page)
    
    # Get the employee list before deletion
    employee_list_before = employees_page.get_employee_list()
    alex_count_before = sum(1 for emp in employee_list_before if "Alex Smith" in emp)
    print(f"Alex Smith count before deletion: {alex_count_before}")
    
    # Delete Alex Smith
    employees_page.delete_employee("Alex Smith")
    
    # Get the employee list after deletion
    employee_list_after = employees_page.get_employee_list()
    alex_count_after = sum(1 for emp in employee_list_after if "Alex Smith" in emp)
    print(f"Alex Smith count after deletion: {alex_count_after}")
    
    # Verify deletion
    assert alex_count_after == 0, f"Alex Smith should be deleted, but found {alex_count_after} instances"
    assert alex_count_before > 0, "Alex Smith should have existed before deletion"