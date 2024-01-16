# -------------------------Selenium webdriver----------------------------------

# Webdriver is a component in selenium
# Webdriver is a module which is available in selenium package
# Webdriver is an API(Application Programming Interface)

# Selenium is for GUI testing
# Postman/Rest assured etc.. are for API testing
# Toad etc are for Database testing

# USER----->GUI/UI(Presentation layer)------>App/Web server(Business logic)----->Database(Backend layer)
#           GUI testing                      API testing                         Database testing

# Automation code---->Webdriver(API)----->Browser(Application under test)
# Download the driver for the browser(ex:chromedriver) to our system

# Architecture of webdriver:
# Selenium3:
# Selenium client library---->JSON(Wire protocol over HTTP)---->Browser drivers---->W3C---->Browsers
# Selenium4:
# Selenium client library---->W3C---->Browser drivers---->W3C---->Browsers

# Setup & configuration of webdriver in pycharm:
# Pre-requisites:
# Python
# Pycharm

# 1)Download browser specific drivers
# Ex: For chrome, download chromedriver
#     For edge, download edgedriver

# 2)Setup selenium webdriver
#    a)Pycharm--->Project settings--->Project interpreter
#    b)pip install selenium==4.0 ---> to install a specific version


# Test case:
# 1)Open web browser
# 2)Open URL(https://admin-demo.nopcommerce.com/login)
# 3)Provide email(admin@yourstore.com)
# 4)Provide password(admin)
# 5)Click on login
# 6)Capture title of dashboard page
# 7)Verify title of page:"Dashboard / nopCommerce administration"(Expected)
# 8)Close browser

# Test case2:
# 1)Open webbrowser(chrome/edge)
# 2)Open URL (https://opensource-demo.orangehrmlive.com/)
# 3)Enter Username (Admin)
# 4)Enter Password (admin123)
# 5)Click on login
# 6)Capture title of home page (Actual title)
# 7)Verify title of the page: OrangeHRM (Expected)
# 8)Close browser

# Selenium3 standards for test case2:

# from selenium import webdriver
#
# driver = webdriver.Chrome("C:\WebDrivers\chromedriver")

# Selenium4 standards for testcase2:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
## driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
actualTitle = driver.title
exp_title = "OrangeHRM"
if actualTitle == exp_title:
    print("Login test passed")
else:
    print("Login test failed")
driver.close()
