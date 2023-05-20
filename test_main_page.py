from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLoginFormMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_should_be_login_form(self, browser):
        link = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_url()
        page.should_be_login_form()


def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.check_the_basket_empty()





