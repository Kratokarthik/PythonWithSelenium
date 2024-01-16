#------------------FindElement Vs FindElements-------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

## find_element() - returns single webelement

#1)Locator matching with single webelement
# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Apple MacBook Pro 13-inch")
# time.sleep(5)

# 2)Locator matching with multiple webelements
# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)
# time.sleep(5)

# 3)Element not available then throws NoSuchElementException
# login=driver.find_element(By.XPATH,"//a[normalize-space()='Loin']")
# login.click()

## find_elements() - returns multiple webelements
                #    returns webelement in the form of a list()

#1)Locator matching with single webelement
# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))
# elements[0].send_keys("Apple MacBook Pro 13-inch")

# 2)Locator matching with multiple webelements
# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))
## print(elements[0].text)
# for ele in elements:
#     print(ele.text)

# 3)Element not available - Zero
login=driver.find_elements(By.XPATH,"//a[normalize-space()='Loin']")
print(len(login))
