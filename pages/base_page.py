from playwright.sync_api import expect
from utils.waits import wait_visible


class BasePage:
    
    url = None

    def __init__(self, page):
        self.page = page

    def open(self):
        if not hasattr(self, "url"):
            raise NotImplementedError(f"{self.__class__.__name__} must define a 'url' attribute")
        self.page.goto(self.url)

    def text_of(self, locator):
        wait_visible(locator)
        return locator.inner_text()

    def is_visible(self, locator):
        return locator.is_visible()