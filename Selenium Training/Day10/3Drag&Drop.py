import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
act=ActionChains(driver)

stockholm_ele=driver.find_element(By.XPATH,"//div[@id='box2']")
sweden_ele=driver.find_element(By.XPATH,"//div[@id='box102']")
act.drag_and_drop(stockholm_ele,sweden_ele).perform()  #drag and drop

rome_ele=driver.find_element(By.XPATH,"//div[@id='box6']")
italy_ele=driver.find_element(By.XPATH,"//div[@id='box106']")
act.drag_and_drop(rome_ele,italy_ele).perform()  #drag and drop