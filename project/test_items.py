def test_button_add_basket(browser):
	link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	browser.get(link)
	button = browser.find_element_by_class_name("btn-add-to-basket").text
	assert button == 'Ajouter au panier'
