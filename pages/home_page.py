from Telvero.components.header import Header
from Telvero.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, browser):
        # Header at top of page.
        self.header = Header(browser)

        # Any extra elements to work with on home page.
        # Home page text elements.
        self.home_head = Element(browser, By.XPATH, "//h1/*[contains(text(), 'Text Your Customers.')]")
        self.home_our_app = Element(browser, By.XPATH, "//*[contains(text(), 'Your phone number. Our app.')]")
        self.home_exp_matters = Element(browser, By.XPATH, "//*[contains(text(), 'Experience Matters')]")
        # Why Telvero text elements.
        self.why_telv_head = Element(browser, By.XPATH, "//h1/*[contains(text(), 'Why Telvero?')]")
        self.why_telv_pricing = Element(browser, By.XPATH, "//*[contains(text(), 'Pricing Doesn’t Have to Be Complicated.')]")
        self.why_telv_employees = Element(browser, By.XPATH, "//*[contains(text(), 'Employees Should Text Customers')]")
        # How it Works text elements.
        self.how_works_head = Element(browser, By.XPATH, "//h1/*[contains(text(), 'How it Works')]")
        self.how_works_setting = Element(browser, By.XPATH, "//*[contains(text(), 'Setting Up Your Telvero Account')]")
        self.how_works_can_do = Element(browser, By.XPATH, "//*[contains(text(), 'What Can You Do with Telvero?')]")
        # Features text elements.
        self.features_head = Element(browser, By.XPATH, "//h1/*[contains(text(), 'What you can do')]")
        self.features_platform = Element(browser, By.XPATH, "//*[contains(text(), 'An Easily-Accessible Platform')]")
        self.features_can_do = Element(browser, By.XPATH, "//*[contains(text(), 'What You Can Do with Telvero')]")
        # Pricing text elements.
        self.pricing_head = Element(browser, By.XPATH, "//h1/*[contains(text(), 'Texting is simple.')]")
        self.pricing_why_telv = Element(browser, By.XPATH, "//*[contains(text(), 'Why Telvero?')]")
        self.pricing_cust_love = Element(browser, By.XPATH, "//*[contains(text(), 'Customer Love')]")

        # Try it Free button on every page except Features, id found to be most unique to separate.
        self.try_free_btn = Element(browser, By.ID, "1644891683")
        self.features_try_free_btn = Element(browser, By.ID, "1200878339")

        # 'View Pricing' button on Why Telvero.
        self.view_pricing_btn = Element(browser, By.XPATH, "//a/*[contains(text(), 'View Pricing')]")

    # Header functions.
    def verify_logo_is_visible(self):
        self.header.verify_logo_is_visible()

    def open_home_page(self):
        self.header.open_home_page()

    def open_why_telvero_page(self):
        self.header.open_why_telvero_page()

    def open_how_it_works_page(self):
        self.header.open_how_it_works_page()

    def open_features_page(self):
        self.header.open_features_page()

    def open_prices_page(self):
        self.header.open_prices_page()

    def open_registration_page(self):
        self.header.open_registration_page()

    def open_login_page(self):
        self.header.open_login_page()

    def open_number_to_call(self):
        self.header.open_number_to_call()

    # Home page functions.
    def get_home_header_text(self):
        self.home_head.get_text()

    def get_home_our_app_text(self):
        self.home_our_app.get_text()

    def get_home_exp_matters_text(self):
        self.home_exp_matters.get_text()

    def get_why_telv_header_text(self):
        self.why_telv_head.get_text()

    def get_why_telv_pricing_text(self):
        self.why_telv_pricing.get_text()

    def get_why_telv_employees_text(self):
        self.why_telv_employees.get_text()

    def get_how_works_header(self):
        self.home_head.get_text()

    def get_how_works_setting_text(self):
        self.how_works_setting.get_text()

    def get_how_works_can_do_text(self):
        self.how_works_can_do.get_text()

    def get_features_header(self):
        self.features_head.get_text()

    def get_features_platform_text(self):
        self.features_platform.get_text()

    def get_features_can_do_text(self):
        self.features_can_do.get_text()

    def get_pricing_header(self):
        self.pricing_head.get_text()

    def get_pricing_why_telv_text(self):
        self.pricing_why_telv.get_text()

    def get_pricing_cust_love_text(self):
        self.pricing_cust_love.get_text()

    def click_page_try_free_btn(self):
        self.try_free_btn.click()

    def click_features_page_try_free_btn(self):
        self.features_try_free_btn.click()

    def click_view_pricing_btn(self):
        self.view_pricing_btn.click()
