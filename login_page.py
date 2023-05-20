from pages.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
        assert "login" in login_link, "The 'link' present"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "The login form present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.registration_form), "The registration form present"

    def register_new_user(self):
        username = self.browser.find_element(*LoginPageLocators.email_login)
        username.send_keys("asd@mail.comme")
        password = self.browser.find_element(*LoginPageLocators.password_login)
        password.send_keys("qwezxc564")
        button = self.browser.find_element(*LoginPageLocators.login_button)
        button.click()
        message = self.browser.find_element(*LoginPageLocators.success_login_message)
        assert self.browser.is_elemet_present(message)



