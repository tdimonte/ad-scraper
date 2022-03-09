#Selenium imports
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/tadim/OneDrive/Desktop/dev/projects/dependencies/chromedriver_win32/chromedriver.exe')
driver.get('https://www.facebook.com/')

#Facebook access
email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

email.clear()
password.clear()

email.send_keys('selscraper@gmail.com')
password.send_keys('SeleniumScraper3')
login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()