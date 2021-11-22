import time

def test_add_to_cart_button_is_displayed(browser):
	link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	browser.get(link)
	button = browser.find_element_by_class_name("btn-add-to-basket")
	assert button is not None, "There is no add to basket button on the page"
	time.sleep(30)