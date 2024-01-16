import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element(By.XPATH,"//div[@class='heroSection-buttonContainer_secondaryBtn secondaryBtn']").click()
driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:/Users/karth/Downloads/Telegram Desktop/snehaAdhaar.pdf")
time.sleep(3)