import math

from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoAlertPresentException, TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import BasketLocators


class ProductPage(BasePage):
    def open(self):
        self.browser.get(self.url)

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*BasketLocators.add_button)
        add_to_basket_button.click()

    def should_display_success_message(self):
        assert self.browser.find_elements(*BasketLocators.success_message), "Success message is displayed"

    def should_not_be_success_message(self):
        assert self.is_element_present(*BasketLocators.success_message), "Element is present"

    def should_display_correct_product_name(self):
        product_name_element = self.browser.find_element(*BasketLocators.product_name)
        product_name = product_name_element.text
        success_message_element = self.browser.find_element(*BasketLocators.success_message)
        assert product_name in success_message_element.text, "Product name match the success message"

    def should_display_basket_total(self):
        assert self.is_element_present(*BasketLocators.basket_total), "Basket total message is displayed"

    def should_match_product_price(self):
        basket_total_element = self.browser.find_element(*BasketLocators.basket_total)
        basket_total = basket_total_element.text
        success_price_element = self.browser.find_element(*BasketLocators.success_price)
        assert basket_total in success_price_element.text, "Product price match the basket total"

    # def should_dissapear(self):
    #     assert self.is_disappeared(*BasketLocators.success_message), "Element is still visible"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    #
    # def is_disappeared(self, locator):
    #     try:
    #         WebDriverWait(self.browser).until(EC.invisibility_of_element_located(locator))
    #         return True
    #     except TimeoutException:
    #         return False
    #     except NoSuchElementException:
    #         return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
