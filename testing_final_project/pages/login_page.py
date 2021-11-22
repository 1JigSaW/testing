from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not valid url"

    def should_be_login_form(self):
        assert self.is_element_presented(*LoginPageLocators.LOGIN_FORM), "Login \
        form is not presented"

    def should_be_register_form(self):
        assert self.is_element_presented(*LoginPageLocators.REGISTER_FROM), "Register \
        form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        password_field_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_2)
        password_field_2.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.SUBMIT)
        submit.click()