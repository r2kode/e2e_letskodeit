from pages.home.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):

        self.lp.login("test@email.com", "abcabc")
        isLoginValid = self.lp.verifyLoginSuccessful()
        assert isLoginValid == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.lp.login("someone@somedomain.com", "somePassword")
        isLoginInvalid = self.lp.verifyLoginFailed()
        assert isLoginInvalid == True
