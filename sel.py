# import chromedriver_autoinstaller as chromedriver
# chromedriver.install()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome("C:\\Users\\Robotux\\Downloads\\chromedriver.exe")
driver.get ("https://www.google.lt/")
#time.sleep(5)

print(driver.page_source)
