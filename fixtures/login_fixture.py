import pytest
from pages.login_page import LoginPage


@pytest.fixture()
def login_page(browser_context):
    page = browser_context.new_page()
    lp = LoginPage(page)
    lp.open()
    yield lp
    page.close()