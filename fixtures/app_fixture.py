import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.helpers import get_user_credentials


@pytest.fixture
def app(browser_context):
    """Provides application navigation helpers."""
    class App:
        def __init__(self, ctx):
            self.ctx = ctx
            self.page = ctx.new_page()

        def login(self, username, password):
            lp = LoginPage(self.page)
            lp.open()
            lp.login(username, password)
            return HomePage(self.page)

        def is_logged_in(self):
            return "Employees" in self.page.content()

    app = App(browser_context)
    yield app
    app.page.close()

@pytest.fixture
def home(app):
    """Provides a logged-in HomePage instance."""
    if not app.is_logged_in():
        username, password = get_user_credentials("admin")
        return app.login(username, password)
    return HomePage(app.page)