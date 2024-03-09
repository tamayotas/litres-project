import os
from selene import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from litres_project.utils import allure_attach
from dotenv import load_dotenv

DEFAULT_BROWSER_VERSION = "100.0"
DEFAULT_BROWSER_NAME = "chrome"


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--browser_version", default="100.0")
    parser.addoption("--browser_name", default="chrome")


@pytest.fixture(scope='function', autouse=True)
def browser_config(request):
    base_url = os.getenv('BASE_URL')
    url_selenoid = os.getenv('URL_SELENOID')

    browser_version = request.config.getoption("--browser_version")
    browser_version = (
        browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    )
    browser_name = request.config.getoption("--browser_name")
    browser_name = (
        browser_name if browser_name != "" else DEFAULT_BROWSER_NAME
    )
    browser.config.base_url = base_url
    browser.config.window_width = 1440
    browser.config.window_height = 900
    options = Options()

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument(
        "--disable-notifications-prompt"
    )

    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {"enableVNC": True,
                             "enableVideo": True
                             },
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"{url_selenoid}/wd/hub",
        options=options,
    )
    browser.config.driver = driver

    yield

    allure_attach.add_screenshot(browser)
    allure_attach.add_html(browser)
    allure_attach.add_logs(browser)
    allure_attach.add_video(browser)

    browser.quit()
