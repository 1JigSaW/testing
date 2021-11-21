from selenium.webdriver.common.by import By


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
	BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
	TITLE_BOOK = (By.TAG_NAME, 'h1')
	ALERT_BOOK = (By.CLASS_NAME, 'alertinner')
	PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
	PRICE_BASKET = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")