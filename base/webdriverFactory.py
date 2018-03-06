"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        base_url = "https://letskodeit.teachable.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chorme":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(base_url)

        return driver
