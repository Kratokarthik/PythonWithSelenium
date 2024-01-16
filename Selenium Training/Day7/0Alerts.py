#---------------------------Alerts/Popups--------------------------------

# myalert=driver.switch_to.alert
#
# myalert.text
# myalert.accept()
# myalert.dismiss()


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# opens alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

alert_window=driver.switch_to.alert

print(alert_window.text)
alert_window.send_keys("Krato")
alert_window.accept()   #close alert window by using Ok button
#alert_window.dismiss() #close alert window by using Cancel button
time.sleep(5)
