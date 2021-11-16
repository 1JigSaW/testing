from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

def summa(x, y):
	return str(int(x) + int(y))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	num1 = browser.find_element_by_id('num1')
	num1 = num1.text
	num2 = browser.find_element_by_id('num2')
	num2 = num2.text

	sum_nums = summa(num1, num2)
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(sum_nums)

	button = browser.find_element_by_class_name('btn-default')
	button.click()
finally:
	time.sleep(10)

	browser.quit()
