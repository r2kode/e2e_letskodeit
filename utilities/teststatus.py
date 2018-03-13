from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultlist = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("PASS")
                    self.log.info("Verification successful :: {}".format(resultMessage))
                else:
                    self.resultlist.append("FAILED")
                    self.log.error("Verification failed :: {}".format(resultMessage))
                    self.screenShot(resultMessage)
            else:
                self.resultlist.append("FAILED")
                self.log.error("Verification failed :: {}".format(resultMessage))
                self.screenShot(resultMessage)
        except:
            self.resultlist.append("FAILED")
            self.log.error("Exception occurred")
            self.screenShot(resultMessage)

    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessge):
        self.setResult(result, resultMessge)
        if "FAILED" in self.resultlist:
            self.log.error("{} Failed".format(testName))
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info("{} Passed".format(testName))
            self.resultlist.clear()
            assert True == True
