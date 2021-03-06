from base.basepage import BasePage
import logging
import utilities.custom_logger as cl
import time


class NavigationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _homepage = "navbar-brand"
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']/a"

    def navigateToHomepage(self):
        self.elementClick(self._homepage, "class")

    def navigateToAllCourses(self):
        self.elementClick(self._all_courses, "link")

    def navigetaToMyCourses(self):
        self.elementClick(self._my_courses, "link")

    def navigateToPractice(self):
        self.elementClick(self._practice, "link")

    def navigateToUserSettingsIcon(self):
        userSettingElement = self.waitForElement(self._user_settings_icon, "xpath", pollFrequency=1)
        self.elementClick(element=userSettingElement)
