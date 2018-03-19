from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "qwerty123"), ("Learn Python 3 from scratch", "yippeekiyay"))
    @unpack
    def test_invalidCouponCode(self, courseName, couponCode):
        self.courses.showAllCourses()
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.clickOnEnrollButton()
        self.courses.submitCouponCode(couponCode)

        result = self.courses.verifyCouponCodeInvalid()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
        self.driver.get("https://letskodeit.teachable.com/courses")
