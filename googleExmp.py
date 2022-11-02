from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ser = Service("C:\webdriver\chromedriver.exe")
op = webdriver.chromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.maximize_window()
driver.get("https://www.google.com")

time.sleep(3)

search = driver.find_element(By.NAME, 'q')
search.send_keys('Youtube')
search.send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()

