import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math 

@pytest.fixture(scope="function")
def answer_math():
	answer = math.log(int(time.time()))
	return answer

@pytest.fixture(scope="function")
def browser():
	print("\nstart work browser..")
	browser = webdriver.Chrome()
	yield browser
	print("\nbrowser quit..")
	browser.quit()

@pytest.mark.parametrize('number', ['236895', '236896',
	'236897', '236898', '236899', '236903', '236904', '236905'])
def test_stepic_form_answer(browser, number, answer_math):
	link = f'https://stepik.org/lesson/{number}/step/1'
	browser.get(link)
	answer_input = WebDriverWait(browser, 10).until(
		EC.visibility_of_element_located(
			(By.CLASS_NAME, "ember-text-area"))
	)
	answer_input.send_keys(answer_math)
	button = WebDriverWait(browser, 10).until(
		EC.visibility_of_element_located(
			(By.CLASS_NAME, "submit-submission"))
	)
	button.click()
	correct_input = WebDriverWait(browser, 10).until(
		EC.visibility_of_element_located(
			(By.TAG_NAME, "pre"))
	)
	correct_input = correct_input.text 
	assert correct_input == 'Correct!'
