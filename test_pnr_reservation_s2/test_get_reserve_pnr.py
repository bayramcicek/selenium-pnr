#!/usr/bin/python3.6
# created by cicek on 10.09.2019 15:15

# get PNR from <link - RezvEntry>
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

# nextDay = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%m/%d/%Y")
nextDay = (datetime.datetime.now() + datetime.timedelta(days=5)).strftime("%d")
month = (datetime.datetime.now() + datetime.timedelta(days=5)).strftime("%m")
year = (datetime.datetime.now() + datetime.timedelta(days=5)).strftime("%Y")

# if nextDay has '0' prefix, remove '0'
if nextDay[0] == "0":
    nextDay = nextDay[1]

# if month has '0' prefix, remove '0'
if month[0] == "0":
    month = month[1]

# make browser invisible
options = Options()
options.add_argument("--headless")


class TestGetReservePnr:

    def test_setup(self):
        global browser
        browser = webdriver.Firefox(options=options)
        # browser = webdriver.Firefox()
        browser.implicitly_wait(2)
        browser.maximize_window()

    def test_get_reserve_pnr(self):
        # Test name: test_get_reserve_pnr
        # 1 | open | <link - RezvEntry> |
        browser.get("<link - RezvEntry>")
        # 2 | click | css=#tripTypeArea > label:nth-child(1) |
        browser.find_element(By.CSS_SELECTOR, "#tripTypeArea > label:nth-child(1)").click()
        # 5 | click | id=depPort |
        # browser.find_element(By.ID, "depPort").click() 6 | select | id=depPort |
        # label=Kabul International (KBL) | #depPort > optgroup:nth-child(2) > option:nth-child(1)
        drop_down = browser.find_element(By.ID, "depPort")
        drop_down.find_element(By.XPATH, "//option[. = 'Kabul International (KBL)']").click()
        # 7 | click | css=#depPort > optgroup:nth-child(2) > option:nth-child(1) |  |
        # browser.find_element(By.CSS_SELECTOR, "#depPort > optgroup:nth-child(2) > option:nth-child(1)").click()
        # 8 | click | id=arrPort |
        # browser.find_element(By.ID, "arrPort").click()
        # 9 | select | id=arrPort | label=Mazar-i-Sharif (MZR) |
        # drop_down_arr = browser.find_element(By.ID, "arrPort")
        browser.find_element(By.XPATH, "//*[@id='arrPort']//option[. = 'Mazar-i-Sharif (MZR)']").click()
        # # 10 | click | css=#arrPort > optgroup:nth-child(2) > option |
        # browser.find_element(By.CSS_SELECTOR, "#arrPort > optgroup:nth-child(2) > option").click()
        # 11 | runScript | window.scrollTo(0,0) |
        browser.execute_script("window.scrollTo(0,0)")
        # 12 | click | id="departureDate" |
        select_departure_field = browser.find_element_by_xpath('//*[@id="departureDate"]')
        select_departure_field.click()

        # year
        open_year_field = browser.find_element_by_xpath('//*[@title="Select Year"]')
        open_year_field.click()
        select_year = browser.find_element_by_xpath("//*[contains(text(), " + year + ")]")
        select_year.click()

        # month
        open_month_field = browser.find_element_by_xpath('//*[@title="Select Month"]')
        open_month_field.click()
        select_month = browser.find_element_by_xpath("//*[@value=\"" + month + "/" + year + "\"]")
        select_month.click()

        # select next day
        select_next_day = browser.find_elements_by_xpath('//table[@class="table-condensed"]//tr/td')

        # print([i.text for i in selectNextDay])
        for i in select_next_day:
            if "disabled" not in i.get_attribute("class") and i.text == nextDay:
                i.click()
                break
        # browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
        sleep(1)

        # 13 | click | id=adult |
        browser.find_element(By.XPATH, '//*[@id="adult"]/option[2]').click()
        # 16 | click | id=btnSearch |
        browser.find_element(By.ID, "btnSearch").click()
        # 17 | click | css=.price-button-inside |
        select_day = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".price-button-inside")))
        select_day.click()
        # 18 | click | value="CONTINUE" |
        next_page = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@value="CONTINUE"]')))
        next_page.click()
        sleep(3)
        # 19 | click | id=gender1 |
        browser.find_element(By.ID, "gender1").click()
        # 20 | select | id=gender1 | label=Mr. |
        drop_down = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'gender1')))
        drop_down.find_element(By.XPATH, "//option[. = 'Mr.']").click()
        # 21 | click | css=#gender1 > option:nth-child(2) |
        browser.find_element(By.CSS_SELECTOR, "#gender1 > option:nth-child(2)").click()
        # 22 | click | id=name1 |
        browser.find_element(By.ID, "name1").click()
        # 23 | type | id=name1 | bayram |
        browser.find_element(By.ID, "name1").send_keys("bayram")
        # 24 | click | id=surname1 |
        browser.find_element(By.ID, "surname1").click()
        # 25 | type | id=surname1 | cicek |
        browser.find_element(By.ID, "surname1").send_keys("cicek")
        # 26 | select | id=bday_day_1 | label=1 |
        drop_down = browser.find_element(By.ID, "bday_day_1")
        drop_down.find_element(By.XPATH, "//option[. = '1']").click()
        # 27 | click | css=#bday_day_1 > option:nth-child(2) |
        browser.find_element(By.CSS_SELECTOR, "#bday_day_1 > option:nth-child(2)").click()
        # 28 | click | id=bday_month_1 |
        browser.find_element(By.ID, "bday_month_1").click()
        # 29 | select | id=bday_month_1 | label=January |
        drop_down = browser.find_element(By.ID, "bday_month_1")
        drop_down.find_element(By.XPATH, "//option[. = 'January']").click()
        # 30 | click | css=#bday_month_1 > option:nth-child(2) |
        browser.find_element(By.CSS_SELECTOR, "#bday_month_1 > option:nth-child(2)").click()
        # 31 | click | id=bday_year_1 |
        browser.find_element(By.ID, "bday_year_1").click()
        # 32 | select | id=bday_year_1 | label=2000 |
        drop_down = browser.find_element(By.ID, "bday_year_1")
        drop_down.find_element(By.XPATH, "//option[. = '2000']").click()
        # 33 | click | css=#bday_year_1 > option:nth-child(9) |
        browser.find_element(By.CSS_SELECTOR, "#bday_year_1 > option:nth-child(9)").click()

        # 59 | click | id=frst-tel-number0 |
        browser.find_element(By.ID, "frst-tel-number0").click()
        # 60 | click | id=email0 |
        browser.find_element(By.ID, "frst-tel-number0").send_keys("55 555 5555")
        browser.find_element(By.ID, "email0").click()
        # 61 | type | id=email0 | a@b.com |
        browser.find_element(By.ID, "email0").send_keys("a@b.com")
        sleep(2)

        # 63 | click | id=btnSave |
        browser.find_element(By.ID, 'btnSave').click()
        browser.implicitly_wait(2)
        sleep(10)
        # 64 | click | id=addSSRContinueBTn |
        continue_btn = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'addSSRContinueBTn')))
        continue_btn.click()
        browser.implicitly_wait(2)

        browser.find_element_by_xpath('//*[contains(text(), "RESERVATION")]').click()
        sleep(1)
        for i in range(12):
            browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
        browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)

        for i in range(2):
            browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
        browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
        sleep(5)

        try:
            span_list = browser.find_elements(By.XPATH, '//*[contains(@class, "booking-reference")]/span')
            print("\n\n----------------------1 ADULT RESERVATION----------------------")
            for i in span_list:
                print(i.text)  # print PNR
        except Exception:  # too broad exception clause
            print("Element not found")
            # //*[@id="j_idt18"]/div[5]/div[1]/div[1]/div[1]/div[2]/div[2]/div/span[1]
            # //*[@id="j_idt18"]/div[5]/div[1]/div[1]/div[1]/div[2]/div[2]/div/span[2]
        print("Surname: cicek\n--------------------------------------------------------------\n")
        sleep(1)

    def test_teardown(self):
        # 79 | close |
        browser.close()
        print("test completed")


if __name__ == '__main__':
    pytest.main()

