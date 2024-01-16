# Xpath Axes:

# self
# parent
# child
# ancestor
# descendant

# following
# following-sibling

# preceding
# preceding-sibling

# Axes          Description                                             Syntax
# Child         Traverse all child element of current html tag          //*[attribute='value']/child::tagname
# Parent        Traverse parent element of current html tag             //*[attribute='value']/parent::tagname
# Following     Traverse all element that comes after current tag       //*[attribute='value']/following::tagname
# Preceding     Traverse all nodes that comes before current tag        //*[attribute='value']/preceding::tagname
# Following-    Traverse from current html tag to next sibling tag      //current html tag[attribute='value']/following-sibling::sibling tag[@attribute='value']
#   sibling
#Preceding-     Traverse from current html tag to previous sibling tag  //current html tag[attribute='value']/preceding-sibling::previous tag[@attribute='value']
#  sibling
# Ancestor      Traverse all ancestor elements of current html tag      //*[attribute='value']/ancestor::tagname
# Descendant    Traverse all descendant elements of current tag         //*[attribute='value']/descendant::tagname



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
# values changes everyday with respect to this application,If you want to run this code, check with website and alter the code respectively
driver.maximize_window()

# self
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Shriram Finance')]/self::a").text
# print(text_msg)


#parent
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Shriram Finance')]/parent::td").text
# print(text_msg)
# time.sleep(10)

# child
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Shriram Finance')]/ancestor::tr/child::td").text
# print(text_msg)
#
# children=driver.find_elements(By.XPATH,"//a[contains(text(),'Shriram Finance')]/ancestor::tr/child::td")
# print(len(children))

# Ancestor:
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Shriram Finance')]/ancestor::tr").text
# print(text_msg)

# Descendant:
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Shriram Finance')]/ancestor::tr/descendant::*").text
# print(text_msg)
#
# descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'Shriram Finance')]/ancestor::tr/descendant::*")
# print("Number of descendants:",len(descendants))

# Following:
# following=driver.find_elements(By.XPATH,"//a[contains(text(),'Shriram Finance')]/ancestor::tr/following::*")
# print("Number of following nodes:",len(following))

# Following-sibling:
# followingsibling=driver.find_elements(By.XPATH,"//a[contains(text(),'Shriram Finance')]/ancestor::tr/following-sibling::*")
# print("Number of following sibling nodes:",len(followingsibling))

# Preceding:
# preceding=driver.find_elements(By.XPATH,"//a[contains(text(),'Shriram Finance')]/ancestor::tr/preceding::*")
# print("Number of preceding nodes:",len(preceding))

# Preceding-sibling:
precedingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Shriram Finance')]/ancestor::tr/preceding-sibling::*")
print("Number of preceding sibling nodes:",len(precedingsiblings))

