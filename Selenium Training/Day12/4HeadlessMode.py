# ----------Headless Mode---------

# without seeing UI we can get output; test execute in backend

# we have to wait until script complete in normal mode;
# whereas we can resume our operations parallel in headless mode
# performance is more while using headless mode

#

from selenium import webdriver


def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\WebDrivers\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver

def headless_edge():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\WebDrivers\msedgedriver.exe")
    ops = webdriver.EdgeOptions()
    ops.headless = True
    driver = webdriver.Edge(service=serv_obj, options=ops)
    return driver

#driver1 = headless_chrome()
driver1=headless_edge()
driver1.get("https://demo.nopcommerce.com/")
driver1.maximize_window()
print(driver1.title)
print(driver1.current_url)
driver1.close()
