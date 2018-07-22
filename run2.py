from selenium import webdriver as wd
import time

MAIN_URL = 'https://www.daum.net/'

driver = wd.Chrome(executable_path='./chromedriver.exe')
driver.get(MAIN_URL)

driver.find_element_by_id('id').send_keys('elmo-yun')
driver.find_element_by_class_name('tf_login').send_keys('elmo-yun')