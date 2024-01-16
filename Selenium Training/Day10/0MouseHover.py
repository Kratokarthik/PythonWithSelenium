#-------------------------Mouse operations----------------------------

#-----ActionChains-----
#1)Mouse hover          move_to_element(element)
#2)Right click          context_click(element)
#3)Double click         double_click(element)
#4)Drag & drop          drag_and_drop(source,target)
# Slider                drag_and_drop_by_offset(element,X,Y)

# --Scrolling page--





# Mouse hover:

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
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
admin=driver.find_element(By.XPATH,"//aside[@class='oxd-sidepanel']//li[1]")
driver.implicitly_wait(5)
usermgmt=driver.find_element(By.XPATH,"//span[normalize-space()='User Management']")
users=driver.find_element(By.XPATH,"//ul[@class='oxd-dropdown-menu']//li")
time.sleep(5)

#Mouse hover:

act=ActionChains(driver)
act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()

# in the above example mouse hover functionality won't work due to changes in website

