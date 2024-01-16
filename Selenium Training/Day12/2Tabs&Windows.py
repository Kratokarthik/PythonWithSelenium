import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
#
# regLink=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(regLink)


#New tab- Selenium4: Opens a tab & switches to new tab
# driver.get("https://www.opencart.com")
# driver.switch_to.new_window('tab')
# driver.get("https://www.orangehrm.com")

#New tab- Selenium4: Opens a new browser window & switches to new window
driver.get("https://www.opencart.com")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com")


time.sleep(3)