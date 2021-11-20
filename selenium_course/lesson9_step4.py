from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(x))))

link = 'http://suninjuly.github.io/alert_accept.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_tag_name('button')
	button.click()

	alert = browser.switch_to.alert
	alert.accept()

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



