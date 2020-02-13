from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time


link = "http://suninjuly.github.io/selects1.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    num1 = browser.find_element_by_css_selector("#num1")
    num2 = browser.find_element_by_css_selector("#num2")
    summa = int(num1.text) + int(num2.text)
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(str(summa))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(15)