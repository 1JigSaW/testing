from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	price = WebDriverWait(browser, 10).until(
		EC.text_to_be_present_in_element(
			(By.ID, "price"), '$100')
	)
	print(price)
	button = browser.find_element_by_id('book')
	button.click()

	input_value = browser.find_element_by_id('input_value')
	x = int(input_value.text)
	variable = calc(x)

	input_field = browser.find_element_by_id('answer')
	input_field.send_keys(variable)

	button2 = browser.find_element_by_id('solve')
	button2.click()
finally:
	time.sleep(10)

	browser.quit()