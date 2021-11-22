from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
	def should_not_be_product_in_basket(self):
		assert self.is_not_element_presented(*BasketPageLocators.PRODUCT_ITEMS), \
			"Product is presented, but should not be" 

	def should_alert_empty_basket(self):
		assert self.is_element_presented(*BasketPageLocators.ALERT_EMPTY_BASKET), \
			"Message about empty basket is not presented"

	def should_not_disappered_empty_basket(self):
		assert not self.is_disappeared(*BasketPageLocators.ALERT_EMPTY_BASKET), \
		   "Empty basket not disappered"