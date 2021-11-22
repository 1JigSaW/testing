import pytest
from .pages.product_page import ProductPage
import time

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

@pytest.mark.parametrize("link", links)
def test_guest_can_add_product_to_basket(browser, link):
	link_get = link
	page = ProductPage(browser, link_get)
	page.open()
	page.should_not_be_success_message()
	page.add_to_basket()
	page.should_equal_title_and_alert()
	page.should_equal_price_and_price_basket()
	page.should_not_disappeared_success_message()
