from Telvero.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class SettingsLeftMenu:
    # Defining elements that are in the left menu on page.
    def __init__(self, browser):
        # second row from the left
        self.your_profile_btn = Element(browser, By.XPATH, "//*[@class='settings---menu-items']/div[1]/a")
        self.your_company_btn = Element(browser, By.XPATH, "//*[@class='settings---menu-items']/div[2]/a")
        self.change_pass_btn = Element(browser, By.XPATH, "//*[@class='settings---menu-items']/div[3]/a")
        self.auto_responder_btn = Element(browser, By.XPATH, "//*[@class='settings---menu-items']/div[4]/a")
        self.plan_payment_btn = Element(browser, By.XPATH, "//*[@class='settings---menu-items']/div[5]/a")
        self.team_btn = Element(browser, By.XPATH, "//*[@class='settings---menu-items']/div[6]/a")
        self.phone_numbers_btn = Element(browser, By.XPATH, "//*[@class='settings---menu-items']/div[7]/a")
        self.logout_btn = Element(browser, By.XPATH, "//*[@class='settings---menu-item settings---menu-item-logout']")

        # first column from the left
        self.settings_btn = Element(browser, By.XPATH, "//img[@alt='Settings']")


    # Methods for clicking all of the above elements each.
    def click_your_profile_btn(self):
        self.your_profile_btn.click()

    def click_your_company_btn(self):
        self.your_company_btn.click()

    def click_change_pass_btn(self):
        self.change_pass_btn.click()

    def click_auto_responder_btn(self):
        self.auto_responder_btn.click()

    def click_plan_payment_btn(self):
        self.plan_payment_btn.click()

    def click_team_btn(self):
        self.team_btn.click()

    def click_phone_numbers_btn(self):
        self.phone_numbers_btn.click()

    def click_logout_btn(self):
        self.logout_btn.click()

    def click_settings_btn(self):
        self.settings_btn.click()
