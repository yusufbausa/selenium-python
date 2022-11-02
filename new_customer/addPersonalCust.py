from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from page_object.newCust import newCust
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ser = Service("C:\webdriver\chromedriver.exe")
op = webdriver.chromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

"""OPEN BROWSER"""
driver.maximize_window()
driver.get("http://confins-qa.taf.co.id/confins")
time.sleep(3)

"""LOGIN"""
username = driver.find_element(By.ID, newCust.username)
username.send_keys('AAZ0049')
username.send_keys(Keys.TAB)

pwd = driver.find_element(By.ID, newCust.pwd)
pwd.send_keys('password')

btn_login = driver.find_element(By.ID, newCust.btn_login)
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located(newCust.btn_login)).click()
btn_login.click()
time.sleep(3)

role_marketing = driver.find_element(By.XPATH, newCust.role_marketing)
# WebDriverWait(10).until(EC.visibility_of_element_located(newCust.role_marketing)).click()
role_marketing.click()
time.sleep(3)

"""ACCESSING MENU"""
btn_menu = driver.find_element(By.ID, newCust.btn_menu)
# WebDriverWait(10).until(EC.visibility_of_element_located(newCust.btn_menu)).click()
btn_menu.click()
time.sleep(3)

btn_menu_customer = driver.find_element(By.ID, newCust.btn_menu_customer)
# WebDriverWait(10).until(EC.visibility_of_element_located(newCust.btn_menu_customer)).click()
btn_menu_customer.click()
time.sleep(3)

btn_cust = driver.find_element(By.XPATH, newCust.btn_cust)
# WebDriverWait(10).until(EC.visibility_of_element_located(newCust.btn_cust)).click()
btn_cust.click()
time.sleep(3)


"""ADDING PERSONAL CUSTOMER"""
btn_add_per_cust = driver.find_element(By.ID, newCust.btn_add_per_cust)
# WebDriverWait(10).until(EC.visibility_of_element_located(newCust.btn_add_per_cust)).click()
btn_add_per_cust.click()
time.sleep(3)

"""INSERT CUSTOMER MAIN DATA"""
field_cust_name = driver.find_element(By.ID, newCust.field_cust_name)
field_cust_name.send_keys('Zisimos Valavanis Two')

select_id_type = driver.find_element(By.ID, newCust.select_id_type)
select_id_type.selectByLabel('KTP')

field_id_number = driver.find_element(By.ID, newCust.field_id_number)
field_id_number.send_keys('3171000100010351')

field_id_expired = driver.find_element(By.ID, newCust.field_id_expired)
field_id_expired.send_keys('01/04/2030')

field_birth_place = driver.find_element(By.ID, newCust.field_birth_place)
field_birth_place.send_keys('Jakarta')

field_birth_date = driver.find_element(By.ID, newCust.field_birth_date)
field_birth_date.send_keys('10/10/1990')

field_npwp = driver.find_element(By.ID, newCust.field_npwp)
field_npwp.send_keys('164243933152658')

field_mother_name = driver.find_element(By.ID, newCust.field_mother_name)
field_mother_name.send_keys('Mother')

time.sleep(5)

driver.quit()
