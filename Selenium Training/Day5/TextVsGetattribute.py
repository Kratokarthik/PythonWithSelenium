#-----------Text Vs get_attribute('value')----------

# text   - returns inner text of the element
# get_attribute('value') - get the value of any attribute

# <input id='123' name='xyz'>Email:</input>   ----->Email is inner text
# mostly links are inner text

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/")
emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()
emailbox.send_keys("abc@gmail.com")
print("Result of text:",emailbox.text)          #prints nothing
print("Result of get_attribute():",emailbox.get_attribute('value'))   #prints abc@gmail.com


button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("Result of text:",button.text)                              # prints LOG IN
print("Result of get_attribute():",button.get_attribute('value')) # prints nothing
print("Result of get_attribute():",button.get_attribute('type'))  # prints submit
