from selenium import webdriver
import time
import os


current_dir = os.path.abspath(os.path.dirname(__file__))
link = 'http://suninjuly.github.io/file_input.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	fields = browser.find_elements_by_tag_name('input')
	for field in fields[:3]:
		field.send_keys('lalalal')

	file_field = browser.find_element_by_id('file')
	file_path = os.path.join(current_dir, 'get_method.py')
	file_field.send_keys(file_path)

	button = browser.find_element_by_tag_name('button')
	button.click()
finally:
	time.sleep(10)

	browser.quit()
