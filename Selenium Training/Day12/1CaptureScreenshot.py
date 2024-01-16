import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\karth\\Documents\\PycharmProjects\\Selenium Training\\Day12\\home.png")
# driver.save_screenshot(os.getcwd()+"home.png")    #os.getcwd() - get the current working directory

# driver.get_screenshot_as_file(os.getcwd()+"home.png")
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_base64()