# Count no of rows & columns
# Read specific row & column data
# Read all the rows & columns data
# Read data based on condition(Eg:List book names whose author name is Mukesh)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

##we need to manually write Xpath with help of DOM for these kind of validation

# Count no of rows & columns:
NoRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
NoColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]//th"))
print("Number of Rows:",NoRows)
print("Number of columns:",NoColumns)

# Read specific Rows & column data:
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print("Specific data from table:",data)

# Read all the rows & columns data:
print("Printing all the rows & columns data...")
for r in range(2,NoRows+1):
    for c in range(1,NoColumns+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end="  ")
    print()

# Read data based on condition:(List book name whose author is Mukesh)
print("Read data based on a condition:")
for r in range(2,NoRows+1):
    authName=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authName=="Mukesh":
        bookName=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookName,"  ",authName,"  ",price)

