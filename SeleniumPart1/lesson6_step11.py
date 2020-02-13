from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    input1 = browser.find_element_by_css_selector("""div.first_block > div.first_class > input""")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("""div.first_block > div.second_class > input""")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("""div.first_block > div.third_class > input""")
    input3.send_keys("IvanPetrov@hotmail.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)