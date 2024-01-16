import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
min_slider=driver.find_element(By.XPATH,"//span[1]")
max_slider=driver.find_element(By.XPATH,"//span[2]")

print("Location of sliders before moving.....")
print(min_slider.location)  #{'x': 59, 'y': 250}
print(max_slider.location)  #{'x': 681, 'y': 250}

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,200).perform()
act.drag_and_drop_by_offset(max_slider,-81,200).perform()

print("Location of sliders after moving.....")
print(min_slider.location)  #{'x': 159, 'y': 250}
print(max_slider.location)  #{'x': 600, 'y': 250}
time.sleep(3)