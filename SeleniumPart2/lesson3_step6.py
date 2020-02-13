from selenium import webdriver
import math
import time

link ="http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer").send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)