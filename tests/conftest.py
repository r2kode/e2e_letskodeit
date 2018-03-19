import pytest
from base.webdriverFactory import WebDriverFactory
from pages.home.login_page import LoginPage


@pytest.yield_fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("One time setUp")

    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("One time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operatin system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
