import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging


class Util():

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):

        if info is not None:
            self.log.info("Wait {} seconds for {}".format(sec, info))
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type="letters"):
        alpha_num = ""
        if type == "lower":
            case = string.ascii_lowercase
        elif type == "upper":
            case = string.ascii_uppercase
        elif type == "digits":
            case = string.digits
        elif type == "mix":
            case = string.ascii_uppercase + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        return self.getAlphaNumeric(charCount, "lower")

    def getUniqueNameList(self, listSize=5, itemLength=None):
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyTextContains(self, actualText, expectedText):
        self.log.info("Actual text from application UI --> {}".format(actualText))
        self.log.info("Expected text in UI --> {}".format(expectedText))
        if expectedText.lower() in actualText.lower():
            self.log.info("Text contains verification pass")
            return True
        else:
            self.log.info("Text contains verification failed")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        self.log.info("Actual text in application UI --> {}".format(actualText))
        self.log.info(("Expected text in application UI --> {}".format(expectedText)))
        if actualText.lower() == expectedText.lower():
            self.log.info("Text match verification pass")
            return True
        else:
            self.log.info("Text match verification failed")
            return False

    def verifyListMatch(self, expectedList, actualList):
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
            else:
                return True

