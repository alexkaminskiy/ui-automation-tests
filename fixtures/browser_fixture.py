import os
import pytest
from playwright.sync_api import sync_playwright
from utils.config_loader import load_config


@pytest.fixture(scope="session")
def browser_instance():
    config = load_config()
    with sync_playwright() as p:
        browser = getattr(p, config["browser"]).launch(
            headless=config["headless"],
            slow_mo=config["slowmo"]
        )
        yield browser, config
        browser.close()


@pytest.fixture()
def browser_context(browser_instance, request):
    browser, config = browser_instance

    # ensure dirs exist
    os.makedirs("videos", exist_ok=True)
    os.makedirs("traces", exist_ok=True)

    # sanitize test name for file paths
    test_name = request.node.nodeid.replace("/", "_").replace("::", "_")

    context = browser.new_context(
        base_url=config["base_url"],
        record_video_dir="reports/videos/",
        record_har_path=f"reports/network/{test_name}.har",
    )

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    # save trace only on failure
    failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed
    if failed:
        context.tracing.stop(path=f"reports/traces/{test_name}.zip")
    else:
        context.tracing.stop(path=f"reports/traces/{test_name}.zip")

    context.close()