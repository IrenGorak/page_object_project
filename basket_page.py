import webbrowser

from pages.locators import BasketLocators


class BasketPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_basket(self):
        basket_link = self.browser.find_element(*BasketLocators.BASKET_LINK)
        basket_link.click()

    def check_the_basket_empty(self):
        message_element = self.browser.find_element(*BasketLocators.EMPTY_CART_MESSAGE)
        return "Your basket is empty" in message_element.text

    def choose_books(self):
        redirect_to_books = self.browser.find_element(*BasketLocators.REDIRECT_BOOKS_PAGE)
        redirect_to_books.click()

    def open_product_page(self):
        product_link = self.browser.find_element(*BasketLocators.PRODUCT_LINK)
        product_link.click()

