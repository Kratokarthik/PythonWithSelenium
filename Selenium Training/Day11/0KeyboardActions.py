# Ctrl + A
# Ctrl + C
# Tab
# Ctrl + V


import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("Bienvenido Krato")

act=ActionChains(driver)

# input1----> Ctrl + A   Select the text

# act.key_down(Keys.CONTROL)
# act.send_keys("A")
# act.key_up(Keys.CONTROL)
# act.perform()
# time.sleep(3)

act.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()

# input1 ----> Ctrl + C Copy text
# act.key_down(Keys.CONTROL)
# act.send_keys("C")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("C").key_up(Keys.CONTROL).perform()

# Press Tab key to navigate to input2(second)
# act.send_keys(Keys.TAB)
# act.perform()

act.send_keys(Keys.TAB).perform()

# input2 ---->Ctrl + V paste the text

# act.key_down(Keys.CONTROL)
# act.send_keys("V")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("V").key_up(Keys.CONTROL).perform()






time.sleep(3)