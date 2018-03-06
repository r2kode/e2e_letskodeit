from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTest(unittest.TestCase):

    base_url = "https://letskodeit.teachable.com"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(2)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):

        self.driver.get(self.base_url)

        self.lp.login("test@email.com", "abcabc")
        isLoginValid = self.lp.verifyLoginSuccessful()
        assert isLoginValid == True

        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.driver.get(self.base_url)

        self.lp.login("someone@somedomain.com", "somePassword")
        isLoginInvalid = self.lp.verifyLoginFailed()
        assert isLoginInvalid == True

        # self.driver.quit()
