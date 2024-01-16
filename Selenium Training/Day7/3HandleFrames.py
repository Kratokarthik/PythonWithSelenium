#---------------------------Frames/Iframes---------------------------

# switch_to.frame(name of the frame)
# switch_to.frame(id of the frame)
# switch_to.frame(Webelement)
# switch_to.frame(0)   #index of frame 

# switch_to.default_content()


# Example:
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serv_obj=Service("C:\WebDrivers\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
#
#
# driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
# driver.maximize_window()
#
# driver.switch_to.frame("frm1")
# driver.find_element(By.XPATH,"//a[@title='facebook']").click()
# driver.switch_to.default_content()
#
# driver.switch_to.frame("frm2")
# driver.find_element(By.XPATH,"//a[@title='instagram']").click()
# driver.switch_to.default_content()
#
# driver.switch_to.frame("frm3")
# driver.find_element(By.XPATH,"//a[@title='youtube']").click()


#----Inner frames----

# Example:
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outerFrame=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerFrame)

innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("God of war")
time.sleep(5)
