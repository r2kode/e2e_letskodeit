from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack


class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            print("locator type not supported")
            return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            by_type = self.getByType(locatorType)
            element = self.driver.find_element(by_type, locator)
        except:
            print("Unable to locate element: [{}] :: {} ".format(locatorType, locator))
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Clicked on element: [{}] :: {} ".format(locatorType, locator))
        except:
            print("Unable to click element: [{}] :: {} ".format(locatorType, locator))
            print_stack()

    def sendKeys(self, data, locator, locatorType):
        try:
            self.getElement(locator, locatorType).send_keys(data)
            print("Send data to element: [{}] :: {} ".format(locatorType, locator))
        except:
            print("Unable to send data to element: [{}] :: {} ".format(locatorType, locator))
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                return True
            else:
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementsList = self.driver.find_elements(byType, locator)
            if len(elementsList) > 0:
                return True
            else:
                return False
        except:
            print("element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("waiting for maximum {} seconds for element to be clickabel".format(timeout))
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[
                                     NoSuchElementException,
                                     ElementNotVisibleException,
                                     ElementNotSelectableException
                                 ])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print("Element become clickable")
        except:
            print("Element not appered on page")
            print_stack()
        return element
