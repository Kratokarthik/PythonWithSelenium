# -------------------------------Commands----------------------------------
# 1)Application commands
# 2)Conditional commands
# 3)Browser commands
# 4)Navigational commands
# 5)Wait commands

# --Application commands:--
# get()        -open the app URL
# title()      -to capture the title of the current webpage
# current_url()-to capture the current url of the webpage
# page_source()-to capture the source code of the webpage

# Example:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# serv_obj=Service("C:\WebDrivers\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
#
# driver.get("https://opensource-demo.orangehrmlive.com/")
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)


# --Conditional commands:--      # Returns True/False
#                                accessed only through webelements not through driver
# is_displayed()
# is_enabled()
# is_selected()

# Example:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# serv_obj=Service("C:\WebDrivers\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
#
# driver.get("https://demo.nopcommerce.com/register")
# driver.maximize_window()
#
# # is_displayed()    is_enabled()
# searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# print("Display status:",searchbox.is_displayed())
# print("Enabled status:",searchbox.is_enabled())
#
# # is_selected()
# male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
# female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
#
# print("Default radio button status:...")
# print(male.is_selected())
# print(female.is_selected())
#
# male.click()  # selecting male radio button
#
# print("After selecting male radio button:...")
# print(male.is_selected())
# print(female.is_selected())
#
# time.sleep(5)

# --Browser commands:--
# close()   -close single browser window(driver focused)
# quit()    -closes multiple browser windows(kill the process)

# Example:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# serv_obj=Service("C:\WebDrivers\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
#
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"nopCommerce").click()
# time.sleep(5)
#
# #driver.close()
# driver.quit()

# --Navigational commands:--
# back()
# forward()
# refresh()

# Example:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# serv_obj=Service("C:\WebDrivers\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
#
# driver.get("https://www.flipkart.com/")
# driver.get("https://demo.nopcommerce.com/")
#
# driver.back()       #flipkart
# driver.forward()    #nopcommerce
# driver.refresh()

# --Wait commands:--

# 1)implicitly_wait()
# 2)explicitly_wait()

# time.sleep(time in sec)
#           Simple to use
#           Performance of the script is very poor
#           If the element is not available within the time mentioned, there's a chance of getting an exception

## implicitly_wait()
#           Single statement (driver.implicitly_wait(10))
#           Performance won't be reduced(If the element is available within the time, it proceed to execute further statements)
#           If the element is not available within the time mentioned, there's a chance of getting an exception

# Example:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# serv_obj=Service("C:\WebDrivers\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
#
# driver.get("https://www.google.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# searchbox=driver.find_element(By.NAME,'q')
# searchbox.send_keys("Selenium")
# searchbox.submit()
#
# #time.sleep(5)
# driver.find_element(By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()


## explicitly_wait()
#           Works based on a condition
#           Works more efficiently
#           We need to insert it in multiple places
#           Feels complicated compared to implicitly_wait()

# Example:
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
#mywait = WebDriverWait(driver, 10)  # explicit wait declaration
mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,
                                                                    ElementNotSelectableException,Exception])

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys("Selenium")
searchbox.submit()
searchlink = mywait.until(EC.presence_of_element_located((By.TAG_NAME,'h3')))
searchlink.click()

 


