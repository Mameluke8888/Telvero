from code.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class ChangePasswordPage:
    def __init__(self, browser):
        self.current_password_input = Element(browser, By.NAME, "currentPassword")
        self.new_password_input = Element(browser, By.NAME, "password")
        self.confirm_password_input = Element(browser, By.NAME, "confirmPassword")

        self.update_btn = Element(browser, By.XPATH, "//button[contains(., 'Update')]")
        self.cancel_btn = Element(browser, By.XPATH, "//button[contains(., 'Update')]")

        self.new_password_msg = Element(browser, By.XPATH, "//div[2]/span[2]")
        self.confirm_password_msg = Element(browser, By.XPATH, "//div[3]/span[2]")
        self.general_msg = Element(browser, By.CLASS_NAME, "MuiAlert-message")

    def get_general_message(self):
        return self.general_msg.get_text()

    def get_new_password_message(self):
        return self.new_password_msg.get_text()

    def get_confirm_password_message(self):
        return self.confirm_password_msg.get_text()

    def click_update_btn(self):
        self.update_btn.click()

    def click_cancel_btn(self):
        self.cancel_btn.click()

    def enter_current_password(self, password):
        self.current_password_input.enter_text(password)

    def enter_new_password(self, password):
        self.new_password_input.enter_text(password)

    def enter_confirm_password(self, password):
        self.confirm_password_input.enter_text(password)
