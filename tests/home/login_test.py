from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):

        self.lp.login("test@email.com", "abcabc")
        verifyTitle = self.lp.verifyLoginTitle()
        self.ts.mark(verifyTitle, "Title is incorrect")
        isLoginValid = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", isLoginValid, "Login failed")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.lp.login("someone@somedomain.com", "somePassword")
        isLoginInvalid = self.lp.verifyLoginFailed()
        assert isLoginInvalid == True
