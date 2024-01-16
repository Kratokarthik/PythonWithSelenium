#--------------------------Handle Dropdown-------------------------------

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#dob_ele=driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']")
dob=Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']"))

## select is a class from html
## if the webpage doesn't have select tag means go with xpath

## Select option from dropdown
# dob.select_by_visible_text("March")    # familiar option (link text is visible text)
# dob.select_by_value("5")   #value
# dob.select_by_index(9)       #index

# capture all the options & print them
allOptions=dob.options
print(len(allOptions))

# for opt in allOptions:
#     print(opt.text)

# select option from dropdown without using built in method:
for opt in allOptions:
    if opt.text=="October":
        opt.click()
        break

time.sleep(5)