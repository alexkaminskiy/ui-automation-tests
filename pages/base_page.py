from playwright.sync_api import expect, Locator, Page
from typing import Optional
from utils.waits import wait_visible


class BasePage:
    
    url: Optional[str] = None

    def __init__(self, page: Page) -> None:
        """Initialize the page object with a Playwright page instance.

        Args:
            page: The Playwright Page instance to interact with
        """
        self.page = page

    def open(self) -> None:
        """Navigate to the page's URL.

        Raises:
            NotImplementedError: If the page class doesn't define a 'url' attribute
        """
        if not hasattr(self, "url") or self.url is None:
            raise NotImplementedError(f"{self.__class__.__name__} must define a valid 'url' attribute")
        self.page.goto(self.url)

    def text_of(self, locator: Locator) -> str:
        """Get the inner text content of a locator.

        Args:
            locator: The Playwright Locator to get text from

        Returns:
            str: The inner text content of the element
        """
        wait_visible(locator)
        return locator.inner_text()

    def is_visible(self, locator: Locator) -> bool:
        """Check if a locator is visible on the page.

        Args:
            locator: The Playwright Locator to check

        Returns:
            bool: True if the element is visible, False otherwise
        """
        return locator.is_visible()