#-----Locators-----
import time

# Identify elements
# Take action

# Types of Locators:
# id
# name
# linktext
# partiallinktext
# classname
# tagname

# Customized locators:
# Css selectors:-           Syntax:
# Tag ID                    tagname#valueofId
# Tag Class                 tagname.valueofClass
# Tag attribute             tagname[attribute=value]
# Tag class attribute       tagname.valueofClass[attribute=value]

# Xpath:-
# Absolute xpath
# Relative xpath

# <input id='dsds' name='dafafd'> Name: </input>

# <a href="link"> register </a>
# In the above line "register" is a linktext

# Example1:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serv_obj = Service("C:\WebDrivers\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
#
# driver.get("https://facebook.com/")
# #driver.maximize_window()


## id & name locators:
# driver.find_element(By.ID,"email").send_keys("karthikajay1996@gmail.com")
# driver.find_element(By.NAME,"pass").send_keys("ajayaakash")
# driver.find_element(By.NAME,"login").click()
# time.sleep(10)


##linktext & partial link text:
#driver.find_element(By.LINK_TEXT,"Log in").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Log ").click()
#time.sleep(10)

# driver.quit()
# driver.close()

# Example2:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serv_obj=Service("C:\WebDrivers\chromedriver.exe")
#
# driver=webdriver.Chrome(service=serv_obj)
#
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# # time.sleep(15)
#
# links=driver.find_elements(By.TAG_NAME,"a")
# print(len(links))

# Example3:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serv_obj=Service("C:\WebDrivers\chromedriver.exe")
#
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# driver.find_element(By.NAME,"password").send_keys("secret_sauce")
# time.sleep(15)

# Example4:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
#driver.get("https://ultimateqa.com/automation")
driver.maximize_window()

#Tag & ID:
# #driver.find_element(By.CSS_SELECTOR,"div#header-sec").click()
# driver.find_element(By.CSS_SELECTOR,"#header-sec").click()    #tag is optional
# time.sleep(15)

#Tag & Class
# #space in classname doesn't work sometimes,we need to trim the elements post space
# driver.get("https://facebook.com/")
# #driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("karthikajay1996@gmail.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("karthikajay1996@gmail.com")     #tag is optional
# time.sleep(15)

# Tag & attribute:
# driver.get("https://facebook.com/")
# #driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("karthikajay1996@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("karthikajay1996@gmail.com")    #tag is optional
# time.sleep(15)

# Tag,Class & Attribute:
driver.get("https://facebook.com/")
#driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("karthikajay1996@gmail.com")
driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_email]").send_keys("karthikajay1996@gmail.com")    #tag is optional
time.sleep(15)
