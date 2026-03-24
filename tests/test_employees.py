from utils.helpers import get_user_credentials
from pathlib import Path
import pytest
from pages.employees_page import EmployeesPage
from pages.add_employee_page import AddEmployeePage

@pytest.mark.smoke
def test_add_new_employee(app):
    username, password = get_user_credentials("admin")
    home = app.login(username, password)
    home.go_to_employees()

    emp_page = EmployeesPage(app.page)
    emp_page.open_add_employee()

    add_page = AddEmployeePage(app.page)
    add_page.add_employee("John Smith", 24, 5000, 24, 3, "john@doe.com")

    assert 1 == 2

    # TODO: Add assertion to verify employee was added successfully
    # employees = emp_page.get_employee_list()
    # assert any("John Smith" in row for row in employees)
