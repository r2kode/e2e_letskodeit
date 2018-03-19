import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_box = "search-courses"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "course-listing-title"
    _all_courses_link = "//a[@href='/courses']"
    _enroll_button = "enroll-button-top"
    _coupon_code_link = "add_coupon"  # id
    _coupon_code_field = "coupon_code"  # id
    _coupon_code_verify_btn = "verify-coupon-code"  # id
    _coupon_code_msg_invalid = "//div[contains(@class, 'spc__inline-form-error') and contains(text(), 'Invalid Coupon')]"
    _cc_num = "cc_field"
    _cc_exp = "cc-exp"
    _cc_cvv = "cc_cvc"
    _submit_enroll = "//div[@id='new_card']//button[contains(text(),'Enroll in Course')]"
    _enroll_error_message = "//div[@id='new_card']//div[contains(text(),'The card number is not a valid credit card number.')]"

    def showAllCourses(self):
        self.elementClick(self._all_courses_link, "xpath")

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box)

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(self._course.format(fullCourseName), "xpath")

    def clickOnEnrollButton(self):
        self.elementClick(self._enroll_button)

    def enterCardNum(self, num):
        self.sendKeys(num, self._cc_num)

    def enterCardExp(self, exp):
        self.sendKeys(exp, self._cc_exp)

    def enterCardCVV(self, cvv):
        self.sendKeys(cvv, self._cc_cvv)

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, "xpath")

    def clickAddCouponCodeBtn(self):
        self.elementClick(self._coupon_code_link, "id")

    def enterCouponCode(self, couponCode):
        self.sendKeys(couponCode, self._coupon_code_field, "id")

    def applyCouponCode(self):
        self.elementClick(self._coupon_code_verify_btn, "id")

    def submitCouponCode(self, couponCode):
        self.clickAddCouponCodeBtn()
        self.enterCouponCode(couponCode)
        time.sleep(2)
        self.applyCouponCode()

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webscroll("down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, "xpath")
        result = self.isElementPresent(messageElement)
        return result

    def verifyCouponCodeInvalid(self):
        time.sleep(1)
        return self.isElementDisplayed(self._coupon_code_msg_invalid, "xpath")

