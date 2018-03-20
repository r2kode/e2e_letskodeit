from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage
import logging
import utilities.custom_logger as cl
import time


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    def clickLoginLink(self):
        self.elementClick(self._login_link, "link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, "id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, "id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, "name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        time.sleep(3)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        return self.isElementPresent("//div[@id='navbar']//li[@class='dropdown']/a", "xpath")

    def verifyLoginFailed(self):
        return self.isElementPresent("//div[contains(text(), 'Invalid email or password')]", "xpath")

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigateToUserSettingsIcon()
        logoutLink = self.waitForElement("//div[@id='navbar']//a[@href='/sign_out']", "xpath", pollFrequency=1)
        self.elementClick(element=logoutLink)

