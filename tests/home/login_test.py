from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTest(unittest.TestCase):

    def test_validLogin(self):
        base_url = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get(base_url)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        userIcon = driver.find_element(By.XPATH, "//div[@id='navbar']//span[text()='User Settings']")
        if userIcon is not None:
            print("Login successful")
        else:
            print("Login failed")

        driver.quit()
