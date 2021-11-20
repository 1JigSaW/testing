from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(x))))

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_tag_name('button')
	button.click()

	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

	x = browser.find_element_by_id('input_value')
	x = int(x.text)
	variable = calc(x)

	input_field = browser.find_element_by_id('answer')
	input_field.send_keys(variable)

	button2 = browser.find_element_by_tag_name('button')
	button2.click()
finally:
	time.sleep(10)

	browser.quit()