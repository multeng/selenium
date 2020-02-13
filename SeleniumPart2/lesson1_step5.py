from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    time.sleep(1)
    checkbox = browser.find_element_by_css_selector("""[for="robotCheckbox"]""")
    checkbox.click()
    time.sleep(1)
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)