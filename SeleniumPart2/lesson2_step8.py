import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

with webdriver.Chrome() as browser:
    browser.get(link)
    fname = browser.find_element_by_name("firstname")
    fname.send_keys("Vasya")
    lname = browser.find_element_by_name("lastname")
    lname.send_keys("Pupkin")
    email = browser.find_element_by_name("email")
    email.send_keys("v@pupkin")
    element = browser.find_element_by_css_selector("#file")
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)
