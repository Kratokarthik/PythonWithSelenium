# Example1:
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def chrome_setup():
#     from selenium.webdriver.chrome.service import Service
#     serv_obj = Service("C:\WebDrivers\chromedriver.exe")
#     driver = webdriver.Chrome(service=serv_obj)
#     return driver
#
# driver=chrome_setup()
# driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
#
# time.sleep(10)

# Example2: Save file in default location

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location=os.getcwd()    # get current working directory


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\WebDrivers\chromedriver.exe")

    #download files in desired location
    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)

    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

driver=chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()

time.sleep(10)


