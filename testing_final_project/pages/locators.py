from selenium.webdriver.common.by import By


class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_LINK = (By.PARTIAL_LINK_TEXT, "basket")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")
	EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
	PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
	PASSWORD_FIELD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
	SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
	BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
	TITLE_BOOK = (By.TAG_NAME, 'h1')
	ALERT_BOOK = (By.CSS_SELECTOR, '.alertinner strong')
	PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
	PRICE_BASKET = (By.CSS_SELECTOR, ".alert-noicon.alert-info p strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasketPageLocators():
	PRODUCT_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
	ALERT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")