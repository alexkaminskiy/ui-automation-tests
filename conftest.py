import allure
import pytest

pytest_plugins = [
    "fixtures.browser_fixture",
    "fixtures.app_fixture",
    "fixtures.login_fixture"
]


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("app").page  # page object from your App fixture

        # Attach screenshot
        allure.attach(
            page.screenshot(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach HTML snapshot
        allure.attach(
            page.content(),
            name="page_source",
            attachment_type=allure.attachment_type.HTML
        )

        # Attach page console logs (optional)
        try:
            logs = page.context.browser.logs
        except:
            logs = "No log support"
        allure.attach(
            str(logs),
            name="browser_logs",
            attachment_type=allure.attachment_type.TEXT
        )

        # Attach recorded video
        try:
            video_path = page.video.path()
            allure.attach(
                file=video_path,
                name="video",
                attachment_type=allure.attachment_type.MP4
            )
        except Exception as e:
            print("Video not available:", e)
