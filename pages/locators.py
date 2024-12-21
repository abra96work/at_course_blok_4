from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    BTN_ENTER = (By.NAME, "login_submit")
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")