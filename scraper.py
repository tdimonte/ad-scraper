#Selenium imports
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/tadim/OneDrive/Desktop/dev/projects/dependencies/chromedriver_win32/chromedriver.exe')
driver.get('https://www.instagram.com/')

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.send_keys('SelScraper')
username.send_keys('SeleniumScraper3')