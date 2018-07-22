# pip install selenium
from selenium import webdriver as wd
import time

# 기본 접속 사이트
MAIN_URL = 'http://tour.interpark.com/'

# 브라우저 띄우기
driver = wd.Chrome(executable_path='./chromedriver.exe')
    
# 접속
driver.get(MAIN_URL)

# 캡쳐 (고스트에서 주로 진행을 함)
driver.save_screenshot('main.png')

# 검색 (검색창의 아이디는 : SearchGNBText)
# 사이트 페이지가 로드되는 것(브라우저 메모리에 모드 로드되는 시점)
# 그냥 2초 대기 후 진행
driver.implicitly_wait(2)
driver.find_element_by_id('SearchGNBText').send_keys('파리')

# 검색 클릭
driver.find_element_by_class_name('search-btn').click()

driver.find_element_by_class_name('moreBtn').click()