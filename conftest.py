import allure
import pytest


pytest_plugins = [
    "fixtures.browser_fixture",
    "fixtures.app_fixture",
    "fixtures.login_fixture"
]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to get the report object
    outcome = yield
    report = outcome.get_result()

    # Only after test execution, and only for test failures:
    if report.when == "call" and report.failed:

        # Get Playwright page from fixtures
        page = item.funcargs.get("app").page

        # Screenshot
        try:
            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print("Screenshot error:", e)

        # HTML snapshot
        try:
            allure.attach(
                page.content(),
                name="page-source",
                attachment_type=allure.attachment_type.HTML
            )
        except Exception as e:
            print("Page source error:", e)

        # Video file (if enabled)
        try:
            video_path = page.video.path()
            allure.attach.file(
                video_path,
                name="video",
                attachment_type=allure.attachment_type.MP4
            )
        except Exception as e:
            print("Video error:", e)
