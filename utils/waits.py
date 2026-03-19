from playwright.sync_api import expect


def wait_visible(selector):
    expect(selector).to_be_visible()