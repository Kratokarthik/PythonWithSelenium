from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# click on link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()   #always prefer link text over partial link text
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# find number of links in a webpage:
links=driver.find_elements(By.TAG_NAME,"a")
#links=driver.find_elements(By.XPATH,"//a")

print("Total no of links:",len(links))

# print all the link names:
for link in links:
    print(link.text)