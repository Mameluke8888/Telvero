from Python.InternTelveroTests.components.settings_left_menu import SettingsLeftMenu
from Python.BrainBucketTests.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class Components:
    # Initializing all elements in Plan, Team, and Phone Numbers on user settings page.
    def __init__(self, browser):
        # Left menu options in settings.
        self.settings_left_menu = SettingsLeftMenu(browser)

        # Name of user logged in.
        self.profile_title = Element(browser, By.XPATH, "//p[@class='topbar__avatar-name']")

        # Plan section.
        self.plan_title = Element(browser, By.XPATH, "//*[@class='chat__topbar-name' and contains(text(), 'Plan')]")
        self.upgrade_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Upgrade')]")
        self.subscription_title = Element(browser, By.XPATH, "//*[@class='text-center text-plan-title' and contains(text(), 'Subscription')]")
        self.first_plan_option_title = Element(browser, By.XPATH, "//h5[contains(text(), '1,000 Contacts')]")
        self.second_plan_option_title = Element(browser, By.XPATH, "//h5[contains(text(), '2,500 Contacts')]")
        self.third_plan_option_title = Element(browser, By.XPATH, "//h5[contains(text(), '10,000 Contacts')]")

        # Team section.
        self.team_title = Element(browser, By.XPATH, "//*[@class='chat__topbar-name' and contains(text(), 'Team')]")
        self.add_member_btn = Element(browser, By.XPATH, "//button[contains(text(), 'Add Team Member')]")
        self.first_name_field = Element(browser, By.XPATH, "//input[@name='firstName']")
        self.last_name_field = Element(browser, By.XPATH, "//input[@name='lastName']")
        self.email_field = Element(browser, By.XPATH, "//input[@name='email']")
        self.first_name_error = Element(browser, By.XPATH, "//span[@class='form__form-group-error' and contains(text(), 'First Name field')]")
        self.last_name_error = Element(browser, By.XPATH, "//span[@class='form__form-group-error' and contains(text(), 'Last Name field')]")
        self.email_error = Element(browser, By.XPATH, "//span[@class='form__form-group-error' and contains(text(), 'Email field')]")
        self.delete_second_member = Element(browser, By.XPATH, "//tbody/tr[2]/td[5]/div/img[@alt='delete-icon']")
        self.send_inv_btn = Element(browser, By.XPATH, "//button[@type='submit' and contains(text(), 'Send Invite')]")
        self.team_cancel_btn = Element(browser, By.XPATH, "//button[@type='button' and contains(text(), 'Cancel')]")

        # Phone Number section.
        self.phone_title = Element(browser, By.XPATH, "//*[@class='chat__topbar-name' and contains(text(), 'Phone')]")
        self.add_number_btn = Element(browser, By.XPATH, "//a[contains(text(),'Add Another Number')]")
        self.first_number_option = Element(browser, By.XPATH, "//button[@class='btn-select-phone '][1]")
        self.add_phone_continue_btn = Element(browser, By.XPATH, "//div[5]/div/div[2][contains(text(), 'Phone Numbers')]")
        self.select_phone_title = Element(browser, By.XPATH, "//h1[@class='select-number__title' and contains(text(), 'Select Phone Number')]")
        self.premium_alert_title = Element(browser, By.XPATH, "//*[contains(text(), 'Upgrade Required')]")
        self.premium_alert_continue_btn = Element(browser, By.XPATH, "//*[@class='btn btn-primary w-80 mb-0' and contains(text(), 'Continue')]")
        self.premium_alert_cancel_btn = Element(browser, By.XPATH, "//*[contains(text(), 'Cancel')]")

    # Settings methods here.
    def verify_profile_title_is_visible(self):
        return self.profile_title.wait_until_visible()

    def get_profile_title(self):
        self.profile_title.get_text()

    def get_plan_title(self):
        self.plan_title.get_text()

    def click_upgrade_btn(self):
        self.upgrade_btn.click()

    def get_subscription_title(self):
        self.subscription_title.get_text()

    def get_first_plan_option_title(self):
        self.first_plan_option_title.get_text()

    def get_second_plan_option_title(self):
        self.second_plan_option_title.get_text()

    def get_third_plan_option_title(self):
        self.third_plan_option_title.get_text()

    def get_team_title(self):
        self.team_title.get_text()

    def click_add_member_btn(self):
        self.add_member_btn.click()

    def enter_first_name_field(self, first_name):
        self.first_name_field.enter_text(first_name)

    def enter_last_name_field(self, last_name):
        self.last_name_field.enter_text(last_name)

    def enter_email_field(self, email):
        self.email_field.enter_text(email)

    def get_first_name_error_text(self):
        self.first_name_error.get_text()

    def get_last_name_error_text(self):
        self.last_name_error.get_text()

    def get_email_error_text(self):
        self.email_error.get_text()

    def click_delete_second_member_icon(self):
        self.delete_second_member.click()

    def click_send_inv_btn(self):
        self.send_inv_btn.click()

    def click_team_cancel_btn(self):
        self.team_cancel_btn.click()

    def get_phone_title(self):
        self.phone_title.get_text()

    def click_add_number_btn(self):
        self.add_number_btn.click()

    def click_first_number_option(self):
        self.first_number_option.click()

    def click_add_phone_continue_btn(self):
        self.add_phone_continue_btn.click()

    def get_select_phone_title(self):
        self.select_phone_title.get_text()

    def get_premium_alert_title(self):
        self.premium_alert_title.get_text()

    def click_premium_alert_continue_btn(self):
        self.premium_alert_continue_btn.click()

    def click_premium_alert_cancel_btn(self):
        self.premium_alert_cancel_btn.click()
