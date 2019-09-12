#!/usr/bin/python3.6
# created by cicek on 11.09.2019 11:22

# get PNR from <link - /reservation>
# 1 adult -local machine- (node)

import pytest
import datetime
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

pnr_no = str(input("enter reservation PNR: "))


class TestMakeReservePayment:

    def test_setup(self):
        global browser
        # browser = webdriver.Firefox(options=options)
        browser = webdriver.Firefox()
        browser.implicitly_wait(2)
        browser.maximize_window()

    def test_make_reserve_payment(self):
        # Test name: test_get_reserve_pnr
        # go to <link - /reservation>
        # 1 | open | <link - /reservation> |
        browser.get("<link - /reservation>")
        # 4 | type | id=PNRNo | PNPEVU |
        browser.find_element(By.ID, "PNRNo").send_keys(pnr_no)
        # 6 | type | id=surname | CICEK |
        browser.find_element(By.ID, "surname").send_keys("CICEK")
        # 7 | click | name=btnPNRSearch |  |
        browser.find_element(By.NAME, "btnPNRSearch").click()
        # 8 | click | css=.owl-item:nth-child(1) .color-type-1 |  |
        sleep(2)
        icon = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-print-all")))
        icon.click()
        # 9 | click | css=.ui-button__text > span
        browser.find_element(By.CSS_SELECTOR, ".ui-button__text > span").click()
        # 10 | selectFrame | index=0 |  |
        browser.switch_to.frame(0)
        # 11 | click | id=j_idt27:1:j_idt31 |  |
        browser.find_element(By.ID, "j_idt27:1:j_idt31").click()
        # 12 | mouseOver | id=j_idt27:1:j_idt31 |  |
        element = browser.find_element(By.ID, "j_idt27:1:j_idt31")
        actions = ActionChains(browser)
        actions.move_to_element(element).perform()
        # 13 | mouseOut | id=j_idt27:1:j_idt31 |  |
        element = browser.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(browser)
        actions.move_to_element(element).perform()
        # 14 | click | css=.selectize-input |  |
        browser.find_element(By.CSS_SELECTOR, ".selectize-input").click()
        # 15 | mouseUp | css=.buy__area |  |
        element = browser.find_element(By.CSS_SELECTOR, ".buy__area")
        actions = ActionChains(browser)
        actions.move_to_element(element).release().perform()
        # 14 | click | id=j_idt27:1:card-owner |
        browser.find_element(By.XPATH, '//*[@class="card__info select__card"]//div[@data-value="1213"]').click()
        # browser.find_element(By.ID, "j_idt27:1:card-owner").click()
        # 15 | type | id=j_idt27:1:card-owner | bayram cicek |
        browser.find_element(By.ID, "j_idt27:1:card-owner").send_keys("bayram cicek")
        # 16 | click | id=j_idt27:1:card-number |
        browser.find_element(By.ID, "j_idt27:1:card-number").click()
        # 17 | type | id=j_idt27:1:card-number | 4242424242424242 |
        browser.find_element(By.ID, "j_idt27:1:card-number").send_keys("4242424242424242")


        browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
        for i in range(3):
            browser.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)
        browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)

        browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
        for i in range(5):
            browser.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)
        browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)
        # ------------------------------------------------------------------------
        # 20 | mouseUp | id=paymentTabContainer |
        element = browser.find_element(By.ID, "paymentTabContainer")
        actions = ActionChains(browser)
        actions.move_to_element(element).release().perform()
        # 21 | click | id=j_idt27:1:cvc |
        browser.find_element(By.ID, "j_idt27:1:cvc").click()
        # 22 | type | id=j_idt27:1:cvc | 4242 |
        browser.find_element(By.ID, "j_idt27:1:cvc").send_keys("4242")
        # 23 | click | id=btnBuy |
        browser.find_element(By.ID, "btnBuy").click()
        sleep(15)

    def test_teardown(self):
        # 79 | close |
        browser.close()
        print("test completed")


if __name__ == '__main__':
    pytest.main()

