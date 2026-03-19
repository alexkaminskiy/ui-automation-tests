from playwright.sync_api import expect


def assert_text_in_page(page, text):
    expect(page.locator("body")).to_contain_text(text)