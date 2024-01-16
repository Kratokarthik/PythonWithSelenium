import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# Date of birth
driver.find_element(By.XPATH, "//input[@id='dob']").click()  # opens date picker

datePicker_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
datePicker_month.select_by_visible_text("Aug")  # month

datePicker_year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datePicker_year.select_by_visible_text("1997")

alldates = driver.find_elements(By.XPATH, "(//table[@class='ui-datepicker-calendar'])[1]/tbody/tr/td/a")

for date in alldates:
    if date.text == "18":
        date.click()
        time.sleep(2)
        break
