import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

links = [
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
	pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]


class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
		page = ProductPage(browser, link)   
		page.open()                      
		page.go_to_login_page()
		register = LoginPage(browser, browser.current_url)
		email = str(time.time()) + "@fakemail.org"
		password = str(time.time())
		register.register_new_user(email, password)
		register.should_be_authorized_user()

	def test_user_can_add_product_to_basket(self, browser):
		page = ProductPage(browser, link)  
		page.open()    
		page.add_to_basket()
		page.should_equal_title_and_alert()
		page.should_equal_price_and_price_basket()
		page.should_not_disappeared_success_message()

	def test_user_cant_see_success_message(self, browser):
		page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
		page.open()                      # открываем страницу
		page.should_not_be_success_message()



# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
# 	page = ProductPage(browser, one_link)
# 	page.open()
# 	page.add_to_basket()
# 	page.should_not_be_success_message()

# def test_message_disappeared_after_adding_product_to_basket(browser):
# 	page = ProductPage(browser, one_link)
# 	page.open()
# 	page.add_to_basket()
# 	page.should_not_disappeared_success_message()

# def test_guest_should_see_login_link_on_product_page(browser):
# 	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
# 	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.go_to_login_page()

# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
# 	link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.go_to_basket()
# 	basket_page = BasketPage(browser, browser.current_url)
# 	basket_page.should_not_be_product_in_basket()
# 	basket_page.should_alert_empty_basket()
# 	basket_page.should_not_disappered_empty_basket()
