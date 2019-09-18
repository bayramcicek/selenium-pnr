#!/usr/bin/python3.6
# created by cicek on 18.09.2019 13:25

# flight change from <link /reservation>

import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# # make browser invisible
# options = Options()
# options.add_argument("--headless")

pnr_no = str(input("\nEnter reservation PNR: "))


class TestMakeReservePayment:

    def test_setup(self):
        global browser
        # browser = webdriver.Firefox(options=options)
        browser = webdriver.Firefox()
        browser.implicitly_wait(2)
        browser.maximize_window()

    def test_flight_change(self):
        # Test name: test_flight_change
        # go to <link /reservation>
        # 1 | open | <link /reservation> |
        browser.get("<link /reservation>")
        sleep(3)
        # 2 | type | id=PNRNo | PNPEVU |
        browser.find_element(By.ID, "PNRNo").send_keys(pnr_no)
        # 3 | type | id=surname | CICEK |
        browser.find_element(By.ID, "surname").send_keys("CICEK")
        # 4 | click | name=btnPNRSearch |  |
        browser.find_element(By.NAME, "btnPNRSearch").click()
        sleep(2)

        icon = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@data-name="CHANGE_FLIGHT"]')))
        icon.click()
        sleep(2)

        try:
            browser.find_element(By.XPATH, '//*[contains(text(), "Available")]').click()
        except Exception:  # too broad exception clause
            print("Element not found: There is no flight available")
        sleep(1)

        try:
            browser.find_element(By.XPATH, '//*[contains(text(), "Continue")]').click()
        except Exception:  # too broad exception clause
            print("Element not found")
        sleep(1)

        try:
            browser.find_element(By.XPATH, '//*[@type="submit"]').click()
        except Exception:  # too broad exception clause
            print("Element not found")
        sleep(1)

        try:
            # 5 | click | css=.journey_list:nth-child(1) .flight-table__flight-type-expander:nth-child(1) >
            # .flight-table__flight-type:nth-child(1)
            browser.find_element(By.CSS_SELECTOR,
                                 ".journey_list:nth-child(1) .flight-table__flight-type-expander:nth-child(1) > "
                                 ".flight-table__flight-type:nth-child(1)").click()
        except Exception:  # too broad exception clause
            print("Element not found")
        sleep(10)

        # 6 | runScript | window.scrollTo(0,0) |
        browser.execute_script("window.scrollTo(0,0)")
        sleep(1)
        # 7 | click | css=.next-reissue > span |
        browser.find_element(By.CSS_SELECTOR, ".next-reissue > span").click()
        sleep(1)
        # 8 | click | css=.ui-button__type-4 > span |
        browser.find_element(By.CSS_SELECTOR, ".ui-button__type-4 > span").click()
        sleep(1)

        sleep(5)

    def test_teardown(self):
        # 9 | close |
        browser.close()
        print("test completed")


if __name__ == '__main__':
    pytest.main()
