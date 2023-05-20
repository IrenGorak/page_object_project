
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    login_form = By.ID, "login_form"
    registration_form = By.ID, "register_form"
    email_login = (By.ID, "id_login-username")
    password_login = (By.ID, "id_login-password")
    login_button = (By.CLASS_NAME, "btn-lg")
    success_login_message = (By.CLASS_NAME, "alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketLocators:
    BASKET_LINK = (By.CLASS_NAME, "btn-group")
    EMPTY_CART_MESSAGE = (By.ID, "promotions")
    REDIRECT_BOOKS_PAGE = (By.CLASS_NAME, "dropdown-submenu")
    PRODUCT_LINK = (By.CLASS_NAME, "thumbnail")

    add_button = By.CLASS_NAME, "btn-add-to-basket"
    success_message = By.CLASS_NAME, "alert"
    product_name = By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong"
    basket_total = By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong"
    success_price = By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div"
