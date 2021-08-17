from Telvero.code.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class YourCompanyPage:
    def __init__(self, browser):
        self.company_input = Element(browser, By.NAME, "businessName")
        self.zip_input = Element(browser, By.NAME, "zip")
        self.account_input = Element(browser, By.NAME, "firstName")
        self.notifications_switch = Element(browser, By.NAME, "checkedB")

        self.save_btn = Element(browser, By.XPATH, "//button[contains(., 'Save')]")

        self.zip_msg = Element(browser, By.XPATH, "//div[2]/span[2]")

    def get_zip_message(self):
        return self.zip_msg.get_text()

    def get_account_number(self):
        return self.account_input.get_text()

    def click_save_btn(self):
        self.save_btn.click()

    def click_notifications_switch(self):
        self.notifications_switch.click()

    def enter_company(self, company_name):
        self.company_input.enter_text(company_name)

    def enter_zip(self):
        self.zip_input.enter_text(password)
