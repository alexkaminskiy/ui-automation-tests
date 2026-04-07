import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.helpers import get_user_credentials


@pytest.fixture()
def app(browser_context):
    """Provides application navigation helpers."""
    class App:
        def __init__(self, ctx):
            self.ctx = ctx
            self._page = None

        @property
        def page(self):
            if self._page is None:
                self._page = self.ctx.new_page()
            return self._page

        def login(self, username, password):
            lp = LoginPage(self.page)
            lp.open()
            lp.login(username, password)
            return HomePage(self.page)

        def is_logged_in(self):
            return "/home" in self.page.url  # or check a specific element

    _app = App(browser_context)
    yield _app

    if _app._page:
        _app._page.close()


@pytest.fixture()
def home(app):
    """Provides a logged-in HomePage instance."""
    username, password = get_user_credentials("admin")
    home_page = app.login(username, password)
    yield home_page