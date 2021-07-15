from Python.InternTelveroTests.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


# Header class for handling elements at top of Telvero home page.
class Header:
    # Initializing all elements in header at top of pages.
    def __init__(self, browser):
        # Top-right bar.
        self.login_btn = Element(browser, By.XPATH, "//a/*[contains(text(), 'Login')]")
        self.telvero_num_btn = Element(browser, By.XPATH, "//a/*[contains(text(), '844-TELVERO')]")

        # Bar across top of page left to right.
        self.telvero_logo = Element(browser, By.XPATH, "//*[@alt='Telvero Logo' and @id='1587270928']")
        self.why_telvero_btn = Element(browser, By.XPATH, "//a/*[contains(text(), 'Why Telvero')]")
        self.how_it_works_btn = Element(browser, By.XPATH, "//a/*[contains(text(), 'How it Works')]")
        self.features_btn = Element(browser, By.XPATH, "//a/*[contains(text(), 'Why Telvero')]")
        self.prices_btn = Element(browser, By.XPATH, "//a/*[contains(text(), 'Pricing')]")
        self.try_free_btn = Element(browser, By.XPATH, "//a/*[contains(text(), 'TRY IT FOR FREE')]")

    # Wait until logo is visible.
    def verify_logo_is_visible(self):
        return self.telvero_logo.wait_until_visible()

    # Click logo button, opens home page.
    def open_home_page(self):
        self.telvero_logo.click()

    # Click why telvero button, opens why telvero page.
    def open_why_telvero_page(self):
        self.why_telvero_btn.click()

    # Click how it works button, opens how it works page.
    def open_how_it_works_page(self):
        self.how_it_works_btn.click()

    # Click features button, opens features page.
    def open_features_page(self):
        self.features_btn.click()

    # Click prices button, opens prices page.
    def open_prices_page(self):
        self.prices_btn.click()

    # Click 'TRY IT FOR FREE' button, opens registration page.
    def open_registration_page(self):
        self.try_free_btn.click()

    # Click login button, opens login page.
    def open_login_page(self):
        self.login_btn.click()

    # Click number button, asks for app to call Telvero's number with.
    def open_number_to_call(self):
        self.telvero_num_btn.click()