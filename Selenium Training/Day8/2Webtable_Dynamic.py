import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(5)

#login:
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
driver.implicitly_wait(5)
#Admin-->user management-->Users
driver.find_element(By.XPATH,"//aside[@class='oxd-sidepanel']//li[1]").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH,"//ul[@class='oxd-dropdown-menu']//li").click()
driver.implicitly_wait(5)

rows=len(driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']"))
print(rows)


# still some code left , due to change in application the axes aren't working
