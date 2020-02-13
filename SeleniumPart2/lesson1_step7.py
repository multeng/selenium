from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)
    x = browser.find_element_by_css_selector("#treasure")
    x = x.get_attribute("valuex")
    print(x)
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    time.sleep(1)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    time.sleep(1)
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)