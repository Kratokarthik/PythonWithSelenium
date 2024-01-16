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

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(5)
alertwindow=driver.switch_to.alert
alertwindow.accept()
time.sleep(5)
