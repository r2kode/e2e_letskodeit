from selenium import webdriver


driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(2)
base_url = "https://letskodeit.teachable.com"


def first_run(base_url):
    driver.get(base_url)
    print(driver.title)
    driver.quit()


def second_run(base_url):
    driver.get(base_url)
    print(driver.title)
    driver.quit()


first_run(base_url)
second_run(base_url)
