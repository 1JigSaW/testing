from .pages.product_page import ProductPage


links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
]

@pytest.mark.parametrize("product", links)
def test_guest_can_add_product_to_basket(browser, product):
	link = product
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.should_equal_title_and_alert()
	page.should_equal_price_and_price_basket()
