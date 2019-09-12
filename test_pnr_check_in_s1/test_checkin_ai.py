#!/usr/bin/python3.6
# created by cicek on 5.09.2019 14:50

# check-in: 1 adult from <link checkin/search>

import pytest
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


get_pnr = str(input(" Enter PNR: "))
get_surname = str(input("Enter SURNAME: "))


def test_setup():
    global browser
    browser = webdriver.Firefox()
    browser.implicitly_wait(2)
    browser.maximize_window()


def test_checkin():
    # Test name: Untitled
    # Step # | name | target | value | comment
    # 1 | open | <link checkin/search> |  |
    browser.get("<link checkin/search>")
    # 3 | click | id=PNRNo |  |
    browser.find_element(By.ID, "PNRNo").click()
    # 4 | type | id=PNRNo | ZW80MJ |
    browser.find_element(By.ID, "PNRNo").send_keys(get_pnr)
    # 5 | click | id=surname |  |
    browser.find_element(By.ID, "surname").click()
    # 6 | type | id=surname | SS |
    browser.find_element(By.ID, "surname").send_keys(get_surname)
    # 7 | click | name=btnPNRSearch |  |
    browser.find_element(By.NAME, "btnPNRSearch").click()
    # 8 | click | css=.color-type-8 | available |
    browser.find_element(By.CSS_SELECTOR, ".color-type-8").click()
    # 9 | click | css=.checkin-passenger-next > span |  |
    form_button = browser.find_element(By.XPATH, '//*[@id="passengerSelectForm"]/button')
    browser.execute_script("arguments[0].scrollIntoView();", form_button)
    form_button.click()
    sleep(0.8)
    # 10 | click | css=.hover > .iCheck-helper |  |
    for i in range(10):
        browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
    sleep(1)
    browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    sleep(0.5)
    browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
    sleep(1)
    browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    # 13 | mouseOut | css=.hover > .iCheck-helper |  |
    element = browser.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(browser)
    actions.move_to_element(element).perform()
    # 14 | click | css=.checkin-passenger-next > span |
    browser.find_element(By.XPATH, '//*[@id="passengerSelectForm"]/button').click()
    sleep(0.5)
    # 15 | click | css=.checkin-passenger-next > span |
    browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
    sleep(0.8)
    browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)

    sleep(10)

    browser.find_element_by_xpath('//*[@id="bottomBar"]//div/button[2]').click()
    sleep(0.5)
    browser.find_element_by_xpath('//*[@id="bottomBar"]//div/button[2]').click()
    sleep(0.5)
    browser.find_element_by_xpath('//*[@id="perform"]').click()
    sleep(1)
    modal_alert = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-alert"]/div'
                                                                                         '/div/div[1]/button')))
    modal_alert.click()
    sleep(1)


def test_teardown():
    # 52 | close |
    browser.close()
    print("test completed")


if __name__ == '__main__':
    pytest.main()
