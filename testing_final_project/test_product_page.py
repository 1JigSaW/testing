from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	page = ProductPage(browser, link)
	page.open()
	time.sleep(2)
	page.add_to_basket()
	time.sleep(2)
	page.should_equal_title_and_alert()
	time.sleep(2)
	page.should_equal_price_and_price_basket()
	time.sleep(2)
