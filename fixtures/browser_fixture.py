import pytest
from playwright.sync_api import sync_playwright
from utils.config_loader import load_config


@pytest.fixture(scope="function")
def browser_context():
    config = load_config()
    with sync_playwright() as p:
        browser = getattr(p, config["browser"]).launch(
            headless=config["headless"],
            slow_mo=config["slowmo"]
        )
        context = browser.new_context(
            base_url=config["base_url"],
            record_video_dir="videos/",
            record_har_path="network.har"
        )
        yield context
        context.close()
        browser.close()