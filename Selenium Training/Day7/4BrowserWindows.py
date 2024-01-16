# -----------------------Browser windows-------------------

# switch_to.window(WindowID)

# current_window_handle   ----> return widowID of single browser window
# window_handles          ----> return windowID's of multiple browser window


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)

# windowID=driver.current_window_handle
# print(windowID)   # D40CEB4BC5E61F28AB5CEE32D3C8EDC6
#                   # F29B0F651C300C80F692717ACAC5BD39

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
#driver.find_element(By.CSS_SELECTOR,"a[href='http://www.orangehrm.com']").click()
time.sleep(5)
windowIds = driver.window_handles

# Approach1:
# parentWindowId=windowIds[0]
# childWindowId=windowIds[1]
#
# driver.switch_to.window(childWindowId)
# print("Title of Child Window:",driver.title)
#
# driver.switch_to.window(parentWindowId)
# print("Title of Parent Window:",driver.title)

# Approach2:
# for winId in windowIds:
#     driver.switch_to.window(winId)
#     print(driver.title)

# Approach3:
for winId in windowIds:
    driver.switch_to.window(winId)
    if driver.title=="OrangeHRM" or "OrangeHRM HR Software | OrangeHRM":
        driver.close()