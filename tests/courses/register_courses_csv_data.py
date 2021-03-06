from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
from utilities.read_data import getCSVData
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToHomepage()
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/home/artur/selenium/e2e_letskodeit/testdata.csv"))
    @unpack
    def test_invalidCouponCode(self, courseName, couponCode):
        # self.courses.showAllCourses()
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.clickOnEnrollButton()
        self.courses.submitCouponCode(couponCode)

        result = self.courses.verifyCouponCodeInvalid()
        self.ts.markFinal("test_invalidCouponCode", result, "Coupon code Verification FAILED")

