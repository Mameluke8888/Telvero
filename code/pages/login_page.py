from code.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


# Login Page class for handling elements on login page of Telvero.
class LoginPage:
    # Initializing elements.
    def __init__(self, browser):
        self.login_title = Element(browser, By.XPATH, "//h4[contains(text(), 'Login to your account')]")
        self.email_field = Element(browser, By.XPATH, "//input[@name='email']")
        self.pass_field = Element(browser, By.XPATH, "//input[@name='password']")
        self.remember_me_checkbox = Element(browser, By.XPATH, "//span[contains(text(), 'Remember me')]")
        self.forgot_pass_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Forgot a password')]")
        self.sign_in_btn = Element(browser, By.XPATH, "//button[contains(text(), 'Sign In')]")
        self.create_account_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Create Account')]")

    # Login page methods.
    def verify_login_title_is_visible(self):
        self.login_title.wait_until_visible()

    def get_login_title(self):
        self.login_title.get_text()

    def enter_email_field(self, email):
        self.email_field.enter_text(email)

    def enter_pass_field(self, password):
        self.pass_field.enter_text(password)

    def click_remember_me_checkbox(self):
        self.remember_me_checkbox.click()

    def click_forgot_pass_btn(self):
        self.forgot_pass_btn.click()

    def click_sign_in_btn(self):
        self.sign_in_btn.click()

    def click_create_account_btn(self):
        self.create_account_btn.click()
