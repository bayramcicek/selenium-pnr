#!/usr/bin/python3.6
# created by cicek on 3.09.2019 11:33

# get PNR from <private-link>
# 1 adult -remote machine- (hub)

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
    browser = webdriver.Remote(options=options,
                               command_executor='http://localhost:4444/wd/hub',
                               desired_capabilities={
                                   'browserName': 'firefox',
                                   # 'javascriptEnabled': True
                               })
    browser.implicitly_wait(2)
    browser.maximize_window()


def test_pnr_remote():
    # Test name: test_pnr_remote
    # 1 | open | <private-link> |
    browser.get("<private-link>")
    # 2 | click | css=#tripTypeArea > label:nth-child(1) |  |
    browser.find_element(By.CSS_SELECTOR, "#tripTypeArea > label:nth-child(1)").click()
    # 3 | click | id=depPort |  |
    browser.find_element(By.ID, "depPort").click()
    # 4 | select | id=depPort | label=Kabul International (KBL) |
    drop_down = browser.find_element(By.ID, "depPort")
    drop_down.find_element(By.XPATH, "//option[. = 'Kabul International (KBL)']").click()
    # 5 | click | css=#depPort > optgroup:nth-child(2) > option:nth-child(1) |  |
    browser.find_element(By.CSS_SELECTOR, "#depPort > optgroup:nth-child(2) > option:nth-child(1)").click()
    # 6 | click | id=arrPort |  |
    browser.find_element(By.ID, "arrPort").click()
    # 7 | select | id=arrPort | label=Mazar-i-Sharif (MZR) |
    drop_down = browser.find_element(By.ID, "arrPort")
    drop_down.find_element(By.XPATH, "//option[. = 'Mazar-i-Sharif (MZR)']").click()
    # 8 | click | css=#arrPort > optgroup:nth-child(2) > option |
    browser.find_element(By.CSS_SELECTOR, "#arrPort > optgroup:nth-child(2) > option").click()
    # 9 | runScript | window.scrollTo(0,0) |
    browser.execute_script("window.scrollTo(0,0)")
    # 10 | click | id="departureDate" |
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

    # 11 | click | id=adult |
    browser.find_element(By.ID, "adult").click()
    # 12 | select | id=adult | label=1 |
    drop_down = browser.find_element(By.ID, "adult")
    drop_down.find_element(By.XPATH, "//option[. = '1']").click()
    # 13 | click | css=#adult > option:nth-child(2) |
    browser.find_element(By.CSS_SELECTOR, "#adult > option:nth-child(2)").click()
    # 14 | click | id=btnSearch |
    browser.find_element(By.ID, "btnSearch").click()
    # 15 | click | css=.price-button-inside |
    select_day = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".price-button-inside")))
    select_day.click()
    # 16 | click | value="CONTINUE" |
    next_page = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@value="CONTINUE"]')))
    next_page.click()
    # 17 | click | id=gender1 |
    browser.find_element(By.ID, "gender1").click()
    # 18 | select | id=gender1 | label=Mr. |
    drop_down = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'gender1')))
    drop_down.find_element(By.XPATH, "//option[. = 'Mr.']").click()
    # 19 | click | css=#gender1 > option:nth-child(2) |  |
    browser.find_element(By.CSS_SELECTOR, "#gender1 > option:nth-child(2)").click()
    # 20 | click | id=name1 |
    browser.find_element(By.ID, "name1").click()
    # 21 | type | id=name1 | nn |
    browser.find_element(By.ID, "name1").send_keys("nn")
    # 22 | click | id=surname1 |
    browser.find_element(By.ID, "surname1").click()
    # 23 | type | id=surname1 | ss |
    browser.find_element(By.ID, "surname1").send_keys("ss")
    # 24 | select | id=bday_day_1 | label=1 |
    drop_down = browser.find_element(By.ID, "bday_day_1")
    drop_down.find_element(By.XPATH, "//option[. = '1']").click()
    # 25 | click | css=#bday_day_1 > option:nth-child(2) |
    browser.find_element(By.CSS_SELECTOR, "#bday_day_1 > option:nth-child(2)").click()
    # 26 | click | id=bday_month_1 |
    browser.find_element(By.ID, "bday_month_1").click()
    # 27 | select | id=bday_month_1 | label=January |
    drop_down = browser.find_element(By.ID, "bday_month_1")
    drop_down.find_element(By.XPATH, "//option[. = 'January']").click()
    # 28 | click | css=#bday_month_1 > option:nth-child(2) |
    browser.find_element(By.CSS_SELECTOR, "#bday_month_1 > option:nth-child(2)").click()
    # 29 | click | id=bday_year_1 |
    browser.find_element(By.ID, "bday_year_1").click()
    # 30 | select | id=bday_year_1 | label=2000 |
    drop_down = browser.find_element(By.ID, "bday_year_1")
    drop_down.find_element(By.XPATH, "//option[. = '2000']").click()
    # 31 | click | css=#bday_year_1 > option:nth-child(9) |
    browser.find_element(By.CSS_SELECTOR, "#bday_year_1 > option:nth-child(9)").click()
    # 32 | click | id=frst-tel-number0 |
    browser.find_element(By.ID, "frst-tel-number0").click()
    # 33 | click | id=email0 |
    browser.find_element(By.ID, "frst-tel-number0").send_keys("55 555 5555")
    browser.find_element(By.ID, "email0").click()
    # 34 | type | id=email0 | a@b.com |
    browser.find_element(By.ID, "email0").send_keys("a@b.com")
    # 35 | click | id=smsCheckLabel |
    browser.find_element(By.ID, "smsCheckLabel").click()
    # 36 | click | id=btnSave |
    browser.find_element(By.ID, "btnSave").click()
    sleep(4)
    # 37 | click | id=addSSRContinueBTn |
    continue_btn = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'addSSRContinueBTn')))
    continue_btn.click()
    # 38 | click | id=card-owner |
    browser.find_element(By.ID, "card-owner").click()
    # 39 | type | id=card-owner | aa bb |
    browser.find_element(By.ID, "card-owner").send_keys("aa bb")
    # 40 | click | id=card-number |
    browser.find_element(By.ID, "card-number").click()
    sleep(2)
    # 41 | type | id=card-number | 1111 1111 1111 1111 |
    browser.find_element(By.ID, "card-number").send_keys("1111")
    browser.find_element(By.ID, "card-number").send_keys("1111")
    browser.find_element(By.ID, "card-number").send_keys("1111")
    browser.find_element(By.ID, "card-number").send_keys("1111")
    sleep(1)
    # 42 | click | id=expiry-month |
    browser.find_element(By.ID, "expiry-month").click()
    # 43 | select | id=expiry-month | label=11 |
    drop_down = browser.find_element(By.ID, "expiry-month")
    drop_down.find_element(By.XPATH, "//option[. = '11']").click()
    # 44 | click | css=#expiry-month > option:nth-child(12) |
    browser.find_element(By.CSS_SELECTOR, "#expiry-month > option:nth-child(12)").click()
    # 45 | click | id=expiry-year |
    browser.find_element(By.ID, "expiry-year").click()
    # 46 | select | id=expiry-year | label=2022 |
    drop_down = browser.find_element(By.ID, "expiry-year")
    drop_down.find_element(By.XPATH, "//option[. = '2022']").click()
    # 47 | click | css=#expiry-year > option:nth-child(5) |
    browser.find_element(By.CSS_SELECTOR, "#expiry-year > option:nth-child(5)").click()
    # 48 | click | id=cvc |
    browser.find_element(By.ID, "cvc").click()
    # 49 | type | id=cvc | 111 |
    actions = ActionChains(browser)
    actions.send_keys()
    browser.find_element(By.ID, "cvc").send_keys("111")
    sleep(1)
    # 50 | click | css=.confirm__label:nth-child(1) > label |
    tab = browser.find_element_by_xpath('//*[@id="CREDIT_CARD_tab"]/div[1]/div[3]/div')
    browser.execute_script("arguments[0].scrollIntoView();", tab)
    sleep(0.8)
    tab.click()
    sleep(3)

    browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
    browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
    browser.find_element_by_tag_name('body').send_keys(Keys.TAB)
    sleep(2)
    browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    sleep(2)

    # 51 | click | id=btnBuy |
    browser.find_element(By.ID, "btnBuy").click()
    sleep(4)

    span = browser.find_element_by_xpath('//*[contains(text(), "Reservation (PNR)")]')
    print(span.text)
    pnr = browser.find_element_by_xpath('//*[contains(text(), "ZW")]')
    print(pnr.text)  # print PNR
    print("Surname: ss")


def test_teardown():
    sleep(3)
    # 52 | close |
    browser.close()
    print("test completed")


if __name__ == '__main__':
    pytest.main()
