# from bs4 import BeautifulSoup
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
driver.get("https://economictimes.indiatimes.com/archive.cms")

### Scrape the first 10 articles of 2018 ###

january = driver.find_element_by_xpath("""//*[@id="pageContent"]/div[2]/table/tbody/tr[1]/td/span/div/a[48]""")
january.click()
day = driver.find_element_by_xpath("""//*[@id="calender"]/tbody/tr[2]/td[2]/a""")
day.click()
headlines = driver.find_elements_by_xpath("""//*[@id="pageContent"]/span/table[2]/tbody/tr/td[1]/ul""")
headlines[0].click()
body = driver.find_element_by_xpath("""/html/body/main/div[10]/div/div[1]/div[3]/div/article/div[3]""")
text = body.text()
print(text)

