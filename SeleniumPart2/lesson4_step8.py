from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.implicitly_wait(20)
    browser.get(link)

    price = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer").send_keys(y)
    button = browser.find_element_by_css_selector("#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(10)