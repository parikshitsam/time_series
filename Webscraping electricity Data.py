from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import calendar
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

webdriverpath = "C:/Users/parik/Documents/Data sets/chromedriver"
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(webdriverpath, options=options)
driver.get("https://www.iexindia.com/marketdata/rtm_areaprice.aspx")
select = Select(driver.find_element_by_id('ctl00_InnerContent_ddlInterval'))
select.select_by_visible_text('Daily')
driver.implicitly_wait(3)
select = Select(driver.find_element_by_id('ctl00_InnerContent_ddlPeriod'))
select.select_by_visible_text('-Select Range-')
driver.implicitly_wait(3)


def download_for_period(year, month_number):
    datetime_object = datetime.datetime.strptime(str(month_number), "%m")
    month_name = datetime_object.strftime("%b")

    select = driver.find_element_by_id('ctl00_InnerContent_calFromDate_clickme')
    select.click()
    select = Select(driver.find_element_by_id('scwYears'))
    select.select_by_visible_text(str(year))
    driver.implicitly_wait(3)
    select = Select(driver.find_element_by_id('scwMonths'))
    select.select_by_visible_text(month_name)
    driver.implicitly_wait(3)
    m = driver.find_elements_by_xpath('//*[@id="scwCells"]/tr[1]/td')
    for i in m:
        if i.text == '1':
            i.click()
    driver.implicitly_wait(3)

    last_day = calendar.monthrange(year, month_number)[1]
    select = driver.find_element_by_xpath('//*[@id="ctl00_InnerContent_calToDate_clickme"]')
    select.click()
    select = Select(driver.find_element_by_id('scwYears'))
    select.select_by_visible_text(str(year))
    driver.implicitly_wait(3)
    select = Select(driver.find_element_by_id('scwMonths'))
    select.select_by_visible_text(month_name)
    driver.implicitly_wait(3)
    for i in range(1, 10):
        m = driver.find_elements_by_xpath('//*[@id="scwCells"]/tr[{}]/td'.format(i))
        for j in m:
            if j.text == str(last_day):
                j.click()
        driver.implicitly_wait(3)

    select = driver.find_element_by_xpath('//*[@id="ctl00_InnerContent_btnUpdateReport"]')
    select.click()
    driver.implicitly_wait(13)
    select = driver.find_element_by_xpath('//*[@id="ctl00_InnerContent_reportViewer_ctl05_ctl04_ctl00_ButtonImg"]')
    select.click()
    select = driver.find_element_by_xpath('//*[@id="ctl00_InnerContent_reportViewer_ctl05_ctl04_ctl00_Menu"]/div[1]')
    select.click()


for month in range(6, 13):
    download_for_period(2020, month)
# select = driver.find_element_by_xpath('//*[@id="ctl00_InnerContent_calToDate_clickme"]')
# select.click()
# select = Select(driver.find_element_by_id('scwYears'))
# select.select_by_visible_text('2021')
# driver.implicitly_wait(3)
# select = Select(driver.find_element_by_id('scwMonths'))
# select.select_by_visible_text('Jan')
# driver.implicitly_wait(3)
# m = driver.find_elements_by_xpath('//*[@id="scwCells"]/tr[1]/td')
# trs = driver.find_elements_by_xpath('//*[@id="scwCells"]/tr')
# for tr in range(1,len(trs)):
#     m = driver.find_elements_by_xpath('//*[@id="scwCells"]/tr[{}]/td'.format(tr))
#     last_num = 0
#     last_elem = m[0]
#     for num,i in enumerate(m):
#         if num == 1:
#             continue
#         print(i.text)
#         if int(i.text) < last_num:
#             last_elem.click()
#         last_num = int(i.text)
#         last_elem = i
