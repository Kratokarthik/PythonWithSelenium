import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
driver.maximize_window()

# 1)Select specific checkbox:
driver.find_element(By.XPATH,"//label[normalize-space()='Option 3']").click()

# 2)Select all the checkboxes:
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

#Approch1:
# for i in range(len(checkboxes)):
#     checkboxes[i].click()
#Approach2:
for checkbox in checkboxes:
    checkbox.click()

# 3)Select multiple checkboxes by choice:
# for checkbox in checkboxes:
#     option = checkbox.get_attribute('value')
#     if option == 'option-1' or option == 'option-3':
#         checkbox.click()

# 4)Select last 2 checkboxes:
# for i in range(len(checkboxes)-2,len(checkboxes)):        # range(2,4)----->3,4
#     checkboxes[i].click()

# 5)Select first 2 checkboxes:
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

# 6)Clearing all the checkboxes:        # before running this enable Approach 2
time.sleep(5)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()





