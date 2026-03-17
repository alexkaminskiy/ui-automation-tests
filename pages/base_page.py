from utils.waits import wait_visible


class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self):
        if hasattr(self, "url"):
            self.page.goto(self.url)

    def text_of(self, selector):
        return selector.inner_text()