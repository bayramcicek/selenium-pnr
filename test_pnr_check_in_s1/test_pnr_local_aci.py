#!/usr/bin/python3.6
# created by cicek on 5.09.2019 15:08

# get PNR from <link RezvEntry>
# 1 adult + 1 child + 1 infant -local machine- (node)

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

# nextDay = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%m/%d/%Y")
nextDay = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d")
month = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%m")
year = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y")

# if nextDay has '0' prefix, remove '0'
if nextDay[0] == "0":
    nextDay = nextDay[1]

# if month has '0' prefix, remove '0'
if month[0] == "0":
    month = month[1]

# make browser invisible
options = Options()
options.add_argument("--headless")


def test_setup():
    global browser
    browser = webdriver.Firefox(options=options)
    # browser = webdriver.Firefox()
    browser.implicitly_wait(2)
    browser.maximize_window()


def test_pnr_local():
    # Test name: test_pnr_local
    # 1 | open | <link RezvEntry> |
    browser.get("<link RezvEntry>")
    # 2 | click | css=#tripTypeArea > label:nth-child(1) |
    browser.find_element(By.CSS_SELECTOR, "#tripTypeArea > label:nth-child(1)").click()
    # 3 | click | css=#child > option:nth-child(2) |
    browser.find_element(By.CSS_SELECTOR, "#child > option:nth-child(2)").click()
    # 4 | click | css=#infant > option:nth-child(2) |
    browser.find_element(By.CSS_SELECTOR, "#infant > option:nth-child(2)").click()
    # 5 | click | id=depPort |
    browser.find_element(By.ID, "depPort").click()
    # 6 | select | id=depPort | label=Kabul International (KBL) |
    drop_down = browser.find_element(By.ID, "depPort")
    drop_down.find_element(By.XPATH, "//option[. = 'Kabul International (KBL)']").click()
    # 7 | click | css=#depPort > optgroup:nth-child(2) > option:nth-child(1) |  |
    browser.find_element(By.CSS_SELECTOR, "#depPort > optgroup:nth-child(2) > option:nth-child(1)").click()
    # 8 | click | id=arrPort |
    browser.find_element(By.ID, "arrPort").click()
    # 9 | select | id=arrPort | label=Mazar-i-Sharif (MZR) |
    drop_down = browser.find_element(By.ID, "arrPort")
    drop_down.find_element(By.XPATH, "//option[. = 'Mazar-i-Sharif (MZR)']").click()
    # 10 | click | css=#arrPort > optgroup:nth-child(2) > option |
    browser.find_element(By.CSS_SELECTOR, "#arrPort > optgroup:nth-child(2) > option").click()
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
    browser.find_element(By.ID, "adult").click()
    # 14 | select | id=adult | label=1 |
    drop_down = browser.find_element(By.ID, "adult")
    drop_down.find_element(By.XPATH, "//option[. = '1']").click()
    # 15 | click | css=#adult > option:nth-child(2) |
    browser.find_element(By.CSS_SELECTOR, "#adult > option:nth-child(2)").click()
    # 16 | click | id=btnSearch |
    browser.find_element(By.ID, "btnSearch").click()
    # 17 | click | css=.price-button-inside |
    select_day = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".price-button-inside")))
    select_day.click()
    # 18 | click | value="CONTINUE" |
    next_page = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@value="CONTINUE"]')))
    next_page.click()
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

    ###
    browser.find_element(By.ID, "name2").click()
    # 34 | type | id=name2 | childname |
    browser.find_element(By.ID, "name2").send_keys("childname")
    # 35 | click | id=surname2 |
    browser.find_element(By.ID, "surname2").click()
    # 36 | type | id=surname2 | childsurname |
    browser.find_element(By.ID, "surname2").send_keys("childsurname")
    # 37 | click | id=bday_day_2 |
    browser.find_element(By.ID, "bday_day_2").click()
    # 38 | select | id=bday_day_2 | label=5 |
    drop_down = browser.find_element(By.ID, "bday_day_2")
    drop_down.find_element(By.XPATH, "//option[. = '5']").click()
    # 39 | click | css=#bday_day_2 > option:nth-child(6) |
    browser.find_element(By.CSS_SELECTOR, "#bday_day_2 > option:nth-child(6)").click()
    # 40 | select | id=bday_month_2 | label=April |
    drop_down = browser.find_element(By.ID, "bday_month_2")
    drop_down.find_element(By.XPATH, "//option[. = 'April']").click()
    # 41 | click | css=#bday_month_2 > option:nth-child(5) |
    browser.find_element(By.CSS_SELECTOR, "#bday_month_2 > option:nth-child(5)").click()
    # 42 | select | id=bday_year_2 | label=2017 |
    drop_down = browser.find_element(By.ID, "bday_year_2")
    drop_down.find_element(By.XPATH, "//option[. = '2017']").click()
    # 43 | click | css=#bday_year_2 > option:nth-child(2) |
    browser.find_element(By.CSS_SELECTOR, "#bday_year_2 > option:nth-child(2)").click()
    # 44 | click | id=infant-a3 |
    browser.find_element(By.ID, "infant-a3").click()
    # 45 | select | id=infant-a3 | label=1. Passenger |
    drop_down = browser.find_element(By.ID, "infant-a3")
    drop_down.find_element(By.XPATH, "//option[. = '1. Passenger']").click()
    # 46 | click | css=#infant-a3 > option:nth-child(2) |
    browser.find_element(By.CSS_SELECTOR, "#infant-a3 > option:nth-child(2)").click()
    # 47 | click | id=name3 |
    browser.find_element(By.ID, "name3").click()
    # 48 | type | id=name3 | infantname |
    browser.find_element(By.ID, "name3").send_keys("infantname")
    # 49 | click | id=surname3 |
    browser.find_element(By.ID, "surname3").click()
    # 50 | type | id=surname3 | infantsurname |
    browser.find_element(By.ID, "surname3").send_keys("infantsurname")
    # 51 | click | id=bday_day_3 |
    browser.find_element(By.ID, "bday_day_3").click()
    # 52 | select | id=bday_day_3 | label=6 |
    drop_down = browser.find_element(By.ID, "bday_day_3")
    drop_down.find_element(By.XPATH, "//option[. = '6']").click()
    # 53 | click | css=#bday_day_3 > option:nth-child(7) |
    browser.find_element(By.CSS_SELECTOR, "#bday_day_3 > option:nth-child(7)").click()
    # 54 | select | id=bday_month_3 | label=May |
    drop_down = browser.find_element(By.ID, "bday_month_3")
    drop_down.find_element(By.XPATH, "//option[. = 'May']").click()
    # 55 | click | css=#bday_month_3 > option:nth-child(6) |
    browser.find_element(By.CSS_SELECTOR, "#bday_month_3 > option:nth-child(6)").click()
    # 56 | click | id=bday_year_3 |
    browser.find_element(By.ID, "bday_year_3").click()
    # 57 | select | id=bday_year_3 | label=2019 |
    drop_down = browser.find_element(By.ID, "bday_year_3")
    drop_down.find_element(By.XPATH, "//option[. = '2019']").click()
    # 58 | click | css=#bday_year_3 > option:nth-child(2) |
    browser.find_element(By.CSS_SELECTOR, "#bday_year_3 > option:nth-child(2)").click()
    ###

    # 59 | click | id=frst-tel-number0 |
    browser.find_element(By.ID, "frst-tel-number0").click()
    # 60 | click | id=email0 |
    browser.find_element(By.ID, "frst-tel-number0").send_keys("55 555 5555")
    browser.find_element(By.ID, "email0").click()
    # 61 | type | id=email0 | a@b.com |
    browser.find_element(By.ID, "email0").send_keys("a@b.com")
    # 62 | click | id=smsCheckLabel |
    browser.find_element(By.ID, "smsCheckLabel").click()
    # 63 | click | id=btnSave |
    browser.find_element(By.ID, "btnSave").click()
    sleep(4)
    # 64 | click | id=addSSRContinueBTn |
    continue_btn = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'addSSRContinueBTn')))
    continue_btn.click()
    # 65 | click | id=card-owner |
    browser.find_element(By.ID, "card-owner").click()
    # 66 | type | id=card-owner | bayram cicek |
    browser.find_element(By.ID, "card-owner").send_keys("bayram cicek")
    # 67 | click | id=card-number |
    browser.find_element(By.ID, "card-number").click()
    sleep(2)
    # 68 | type | id=card-number | 1111 1111 1111 1111 |

    for i in range(4):
        browser.find_element(By.ID, "card-number").send_keys("1111")

    sleep(1)
    # 69 | click | id=expiry-month |
    browser.find_element(By.ID, "expiry-month").click()
    # 70 | select | id=expiry-month | label=11 |
    drop_down = browser.find_element(By.ID, "expiry-month")
    drop_down.find_element(By.XPATH, "//option[. = '11']").click()
    # 71 | click | css=#expiry-month > option:nth-child(12) |
    browser.find_element(By.CSS_SELECTOR, "#expiry-month > option:nth-child(12)").click()
    # 72 | click | id=expiry-year |
    browser.find_element(By.ID, "expiry-year").click()
    # 73 | select | id=expiry-year | label=2022 |
    drop_down = browser.find_element(By.ID, "expiry-year")
    drop_down.find_element(By.XPATH, "//option[. = '2022']").click()
    # 74 | click | css=#expiry-year > option:nth-child(5) |
    browser.find_element(By.CSS_SELECTOR, "#expiry-year > option:nth-child(5)").click()
    # 75 | click | id=cvc |
    browser.find_element(By.ID, "cvc").click()
    # 76 | type | id=cvc | 111 |
    actions = ActionChains(browser)
    actions.send_keys()
    browser.find_element(By.ID, "cvc").send_keys("111")
    sleep(1)
    # 77 | click | css=.confirm__label:nth-child(1) > label |
    tab = browser.find_element_by_xpath('//*[@id="CREDIT_CARD_tab"]/div[1]/div[3]/div')
    browser.execute_script("arguments[0].scrollIntoView();", tab)
    sleep(0.8)
    tab.click()
    sleep(3)

    for i in range(3):
        browser.find_element_by_tag_name('body').send_keys(Keys.TAB)

    sleep(2)
    browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    sleep(2)

    # 78 | click | id=btnBuy |
    browser.find_element(By.ID, "btnBuy").click()
    sleep(4)

    span = browser.find_element_by_xpath('//*[contains(text(), "Reservation (PNR)")]')
    print(span.text)
    pnr = browser.find_element_by_xpath('//*[contains(text(), "ZW")]')
    print(pnr.text)  # print PNR
    print("Surname: cicek")


def test_teardown():
    # 79 | close |
    browser.close()
    print("test completed")


if __name__ == '__main__':
    pytest.main()
