from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = 'http://suninjuly.github.io/math.html'
	browser = webdriver.Chrome()
	browser.get(link)
	x = browser.find_element_by_id('input_value')
	x = x.text
	variable = calc(x)

	input_field = browser.find_element_by_id('answer')
	input_field.send_keys(variable)

	radio_button = browser.find_element_by_id('robotCheckbox')
	radio_button.click()

	checkbox_button = browser.find_element_by_id('robotsRule')
	checkbox_button.click()

	button = browser.find_element_by_class_name('btn-default')
	button.click()
finally:
	time.sleep(10)

	browser.quit()