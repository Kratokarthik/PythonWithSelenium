#-----Handle Cookies-----
# Cookie is not a webelement
# Cookie has multiple attributes like -----name="xyz"
#                                          value=1234
#                                          expirydate=date
#cookies are stored in dictionary format



import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Capture cookies from the browser
cookies=driver.get_cookies()
print(len(cookies))

# Print details of all the cookies
# for c in cookies:
#     #print(c)
#     print(c.get('name'),":",c.get('expiry'),":",c.get('value'))

# Add new cookie to a browser
# driver.add_cookie({"name":"Mycookie","value":"123456"})
# cookies=driver.get_cookies()
# print(len(cookies))

# Delete a specific cookie from the browser
# driver.delete_cookie("Mycookie")
# cookies=driver.get_cookies()
# print("Size of cookies after delete:",len(cookies))

# Delete all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print('Size of cookies after delete all:',len(cookies))