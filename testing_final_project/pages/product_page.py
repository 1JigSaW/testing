from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def add_to_basket(self):
		add_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
		add_basket.click()
		self.solve_quiz_and_get_code()

	def should_be_get_code_quiz(self):
		pass

	def should_equal_title_and_alert(self):
		title_book = self.browser.find_element(*ProductPageLocators.TITLE_BOOK).text
		alert_book = self.browser.find_element(*ProductPageLocators.ALERT_BOOK).text
		print(title_book)
		print(alert_book)
		assert title_book == alert_book, "Different names"

	def should_equal_price_and_price_basket(self):
		price = self.browser.find_element(*ProductPageLocators.PRICE).text
		price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
		print(price)
		print(price_basket)
		assert price == price_basket, "Different prices"