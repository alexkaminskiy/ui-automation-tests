import allure
import pytest
from utils.helpers import get_user_credentials

@pytest.mark.ui
@allure.title("Verify navigation header")
@allure.description("Test that the homepage header displays the correct heading message")
@allure.feature("Navigation")
@allure.story("Homepage Header")
def test_navigation_header(app, home):
    with allure.step("Login to the application"):
        username, password = get_user_credentials("admin")
        app.login(username, password)
    
    with allure.step("Get heading message from homepage"):
        heading_message = home.get_heading_message()
        allure.attach(f"Heading message: {heading_message}", name="Heading text", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Verify heading contains expected text"):
        assert "Employee Management Built for Scale" in heading_message.replace("\n", " ")