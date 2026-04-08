import pytest
from utils.helpers import get_user_credentials

@pytest.mark.ui
# @pytest.mark.skip(reason="Temp disabled")
def test_navigation_header(app, home):
    username, password = get_user_credentials("admin")
    app.login(username, password)
    heading_message = home.get_heading_message()
    assert "Employee Management Built for Scale" in heading_message.replace("\n", " ")