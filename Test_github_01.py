import time
import saver
from selenium import webdriver
driver = webdriver.Chrome()
saver.init('log1')

saver.test_suite(1)

#    -- ТЕСТ-КЕЙСЫ ДЛЯ КНОПКИ --
# test-case_1 (Если кликнуть по кнопке "blog" открывается страница "Блог")
driver.get('https://www.gobrief.com/')
searchbutton = driver.find_element_by_xpath('/html/body/div[1]/div/div/a[1]').click()
if(driver.current_url == "https://gobrief.com/blog/"):
    saver.test_case(1, True, 'Если кликнуть по кнопке "blog" открывается страница "Блог"')
else:
    saver.test_case(1, False, 'Если кликнуть по кнопке "blog" открывается страница "Блог"')
time.sleep(2)
saver.quit()
driver.close()
driver.quit()