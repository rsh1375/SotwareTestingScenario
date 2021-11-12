from selenium import webdriver
import time
chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()

chrome_browser.get(
    'https://www.digikala.com/')

panel_heading = chrome_browser.find_element_by_css_selector("body > header > div > div > div.c-header__action > div:nth-child(1) > div > a")
panel_heading.click()

element = chrome_browser.find_element_by_xpath("/html/body/main/div[2]/section/div[2]/form/div[4]/label/div/input")
element.send_keys("rsh1375@gmail.com")

panel_heading1 = chrome_browser.find_element_by_css_selector("#loginForm > button")
panel_heading1.click()

element = chrome_browser.find_element_by_xpath("/html/body/main/div[2]/section/div/form/div[2]/div[3]/label/div/input")
element.send_keys("rsh1375@gmail.com")

panel_heading2 = chrome_browser.find_element_by_css_selector("#authForm > button")
panel_heading2.click()

panel_heading3 = chrome_browser.find_element_by_css_selector("body > header > div > div > div.c-header__action > div:nth-child(1) > div > a")
panel_heading3.click()

time.sleep(5)