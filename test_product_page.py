import pytest

from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.locators import BasketLocators
from pages.product_page import ProductPage


@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    # product_page.solve_quiz_and_get_code()
    product_page.should_display_success_message()
    product_page.should_display_correct_product_name()
    product_page.should_display_basket_total()
    product_page.should_match_product_price()


@pytest.mark.need_review
def test_user_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/"
    page = BasketPage(browser, link)
    page.open()
    page.choose_books()
    page.open_product_page()
    page.go_to_basket()
    page.check_the_basket_empty()


@pytest.mark.need_review
def test_user_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_user_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_user_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


class TestUserAddToBasketFromProductPage:
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-girl-who-played-with-non-fire_203/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.is_disappeared(*BasketLocators.success_message)


def test_user_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()
