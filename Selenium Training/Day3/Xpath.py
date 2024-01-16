#------------------------Xpath-----------------------
import time

# Xpath is defined as XML path
# It is a syntax orlanguage for finding any element on the webpage using xml path expression
# Xpath is used to find location of any element on a webpage using HTML DOM structure.
# Xpath can be used to navigate through elements and attributes in DOM.
# Xpath is an address of an element

# DOM - Document Object Model
# It's an API provided by browser
# When a webpage is created, then browser creates a DOM of the page.

# ---Types of Xpath:---

# 1)Absolute xpath/Full xpath
#   Ex:/html/body/nav/div/div[2]/div[1]/div/ul/li[2]/a/button

# 2)Relative/Partial xpath
#   Ex://*[@id="navbarSupportedContent"]/div[1]/div/ul/li[2]/a/button

#Diff between Absolute & Relative Xpaths
# 1)Absolute xpath starts from root html node
#   Relative xpath directly jump to element on DOM
# 2)Absolute xpath start with /
#   Relative xpath start with //
# 3)In Absolute xpath we use only tags/nodes
#   In Relative xpath we use attributes

# How to write xpath manually
# Ex: html/body/div[6]/div[1]/div[2]/div[1]/ul/li[1]/a

# Syntax for writing relative xpath:
# //tagname[@attribute='value']
# Ex: //input[@id='small-searchterms']
#     //*[@id='small-searchterms']

# How to capture xpath automatically:
# 1)Firebug, Firepath ---> Firefox ---->deprecated/not available
# 2)Right click on element--->Inspect--->Highlight html code--->Right click--->Copy xpath
# 3)Selectorshub

# Reasons to prefer relative xpath:
# 1)If dev introduced a new element then absolute xpath will break
# 2)If dev changed the location then absolute xpath will break

# Absolute xpath is unstable...

# Xpath options:
# and
# or
# contains()
# starts-with()
# text()


# Example1:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Absolute xpath
# driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Samsung")
# driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

# Relative xpath
# driver.find_element(By.XPATH,"//*[@id='small-searchterms']").send_keys("Samsung")
# driver.find_element(By.XPATH,"//*[@id='small-search-box-form']/button").click()


# or,and
# driver.find_element(By.XPATH,"//input[@id='small-searchterms' or @name='q']").send_keys("iphone")
# driver.find_element(By.XPATH,"//button[@class='button-1 search-box-button' and @type='submit']").click()


# contains(), starts-with()
# driver.find_element(By.XPATH,"//input[contains(@id,'small')]").send_keys("Nokia")
# driver.find_element(By.XPATH,"//button[starts-with(@type,'sub')]").click()

# text()
driver.find_element(By.XPATH,"//a[text()=' Electronics ']").click()
time.sleep(10)
