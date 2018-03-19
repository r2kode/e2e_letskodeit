from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        fileName = "{}_{}.png".format(resultMessage, str(round(time.time() * 1000)))
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved: {}".format(destinationFile))
        except:
            self.log.error("Unable to save screenshot")
            print_stack()

    def getTitle(self):
        return self.driver.title

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
            self.log.info("{} type not supported".format(locator_type))
            return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            by_type = self.getByType(locatorType)
            element = self.driver.find_element(by_type, locator)
        except:
            self.log.info("Unable to locate element: [{}] :: {} ".format(locatorType, locator))
        return element

    def getElementList(self, locator, locatorType="id"):

        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Found element list with {} of {}".format(locatorType, locator))
        except:
            self.log.info("Not found elements list with {} of {}".format(locatorType, locator))

        return locator

    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element: [{}] :: {} ".format(locatorType, locator))
        except:
            self.log.info("Unable to click element: [{}] :: {} ".format(locatorType, locator))
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Send data '{}' to element: {}={} ".format(data, locatorType, locator))
        except:
            self.log.info("Unable to send data to element: {}={} ".format(locatorType, locator))
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("in locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before getting text")
            text = element.text
            self.log.debug("After getting text of size: {}".format(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText");
            if len(text) != 0:
                self.log.info("Getting text on element {}".format(info))
                self.log.info("Text is: {}".format(text))
                text = text.strip()
        except:
            self.log.error("Failed to get text on element {}".format(info))
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present [{}] :: {}".format(locatorType, locator))
                return True
            else:
                self.log.info("Element not present [{}] :: {}".format(locatorType, locator))
                return False
        except:
            self.log.info("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element displayed [{}] :: {}".format(locatorType, locator))
            else:
                self.log.info("Element not displayed [{}] :: {}".format(locatorType, locator))
            return isDisplayed
        except:
            self.log.info("Element not found")
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
            self.log.info("waiting for maximum {} seconds for element to be clickabel".format(timeout))
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[
                                     NoSuchElementException,
                                     ElementNotVisibleException,
                                     ElementNotSelectableException
                                 ])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element become clickable")
        except:
            self.log.info("Element not appered on page")
            print_stack()
        return element

    def webscroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")
