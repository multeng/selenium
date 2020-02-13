from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get(link)
    x = browser.find_element_by_css_selector("#input_value")
    x = x.text
    y = calc(int(x))
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    button.click()
    time.sleep(10)