#!/usr/bin/python3.6
# created by cicek on 5.09.2019 14:50

# check-in: 1 adult + 1 Infant from <link checkin/search>

import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

get_pnr = str(input(" Enter PNR: "))
get_surname = str(input("Enter SURNAME: "))


class TestCheckinAi:

    def test_setup(self):
        global browser
        browser = webdriver.Firefox()
        browser.implicitly_wait(2)
        browser.maximize_window()

    def test_checkin_ai(self):
        # Test name: test_checkin_ai
        # 1 | open | <link checkin/search> |
        browser.get("<link checkin/search>")
        # 2 | click | id=PNRNo |
        browser.find_element(By.ID, "PNRNo").click()
        # 3 | type | id=PNRNo |
        browser.find_element(By.ID, "PNRNo").send_keys(get_pnr)
        # 4 | click | id=surname |
        browser.find_element(By.ID, "surname").click()
        # 5 | type | id=surname |
        browser.find_element(By.ID, "surname").send_keys(get_surname)
        # 6 | click | name=btnPNRSearch |
        browser.find_element(By.NAME, "btnPNRSearch").click()
        # 7 | click | css=.color-type-8 | available |
        browser.find_element(By.CSS_SELECTOR, ".color-type-8").click()
        # 8 | click |
        form_button = browser.find_element(By.XPATH, '//*[@id="passengerSelectForm"]/button')
        browser.execute_script("arguments[0].scrollIntoView();", form_button)
        form_button.click()
        sleep(0.8)

        for i in range(10):
            browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
        sleep(0.5)

        browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
        sleep(0.5)

        browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
        sleep(1)

        browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)

        element = browser.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(browser)
        actions.move_to_element(element).perform()

        browser.find_element(By.XPATH, '//*[@id="passengerSelectForm"]/button').click()
        sleep(0.5)

        browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
        sleep(0.8)

        browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
        sleep(3)

        for i in range(2):
            browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
        browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
        sleep(2)

        for i in range(3):
            browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
        browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
        sleep(1)

        for i in range(2):
            browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
        browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
        sleep(0.5)

        browser.find_element(By.XPATH, '//*[@id="passengerSelectForm"]/button').click()
        sleep(0.8)

        for i in range(2):
            try:
                browser.find_element(By.XPATH, '//*[@id="bottomBar"]//button[2]').click()
            except Exception:  # too broad exception clause
                print("Element not found")
            sleep(2)

        browser.find_element(By.XPATH, '//*[@id="perform"]').click()

        print("\n\n------------------AI-check-in-DONE-----------------\n\n")
        sleep(1)

    def test_teardown(self):
        # | close |
        browser.close()
        print("test completed")


if __name__ == '__main__':
    pytest.main()
