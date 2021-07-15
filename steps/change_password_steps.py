from behave import given, when, then
import time


from code.webelements.browser import Browser
from code.config_reader import ConfigReader
from code.pages.change_password_page import ChangePasswordPage
from code.pages.login_page import LoginPage
from code.webelements.UIElement import UIElement as Element
from code.webelements.settings_left_menu import SettingsLeftMenu
from selenium.webdriver.common.by import By

URL = "https://app.telvero.com"
configs = ConfigReader("config.ini")


@given("a registered user is successfully logged in")
def launch_profile_page(context):
    browser = Browser(URL, configs.get_browser('environment'), configs.get_wait_time('environment'))
    context.browser = browser
    login_page = LoginPage(browser)
    context.login_page = login_page
    context.user_email = configs.get_email('user1')
    context.user_password = configs.get_password('user1')
    login_page.enter_email_field(context.user_email)
    login_page.enter_pass_field(context.user_password)
    login_page.click_sign_in_btn()


@given("user moves to settings menu by clicking on Settings option from left menu")
def launch_settings_page(context):
    browser = context.browser
    change_password_page = ChangePasswordPage(browser)
    context.change_password_page = change_password_page
    left_menu = SettingsLeftMenu(browser)
    context.left_menu = left_menu
    # left_menu.click_remember_me_checkbox()
    left_menu.click_settings_btn()


@given("user moves to password update page by clicking on Change Password option from left menu")
def open_change_password_page(context):
    left_menu = context.left_menu
    left_menu.click_change_pass_btn()


@when("user types in current password, new password at least 8 symbols long, matched new password confirmation")
def enter_correct_password(context):
    change_password_page = context.change_password_page
    user_password = context.user_password
    change_password_page.enter_current_password(user_password)
    change_password_page.enter_new_password(user_password)
    change_password_page.enter_confirm_password(user_password)


@when("user types incorrect current password, new password at least 8 symbols long, matched new password confirmation")
def enter_correct_password(context):
    change_password_page = context.change_password_page
    user_password = context.user_password
    change_password_page.enter_current_password(user_password + "1")
    change_password_page.enter_new_password(user_password)
    change_password_page.enter_confirm_password(user_password)


@when("user types in current password, new password at least 8 symbols long, unmatched new password confirmation")
def enter_incorrect_confirm(context):
    change_password_page = context.change_password_page
    user_password = context.user_password
    change_password_page.enter_current_password(user_password)
    change_password_page.enter_new_password(user_password)
    change_password_page.enter_confirm_password(user_password + "1")


@when("user types in current password, new password shorter than 8 symbols long, matched new password confirmation")
def enter_short_password(context):
    change_password_page = context.change_password_page
    user_password = context.user_password
    change_password_page.enter_current_password(user_password)
    change_password_page.enter_new_password("1234567")
    change_password_page.enter_confirm_password("1234567")


@when("user types in current password, new password at least 8 symbols long, no new password confirmation")
def enter_no_confirm(context):
    change_password_page = context.change_password_page
    user_password = context.user_password
    change_password_page.enter_current_password(user_password)
    change_password_page.enter_new_password("12345678")
    change_password_page.enter_confirm_password("")


@when("user types in current password, no new password, no new password confirmation")
def enter_no_confirm(context):
    change_password_page = context.change_password_page
    user_password = context.user_password
    change_password_page.enter_current_password(user_password)
    change_password_page.enter_new_password("")
    change_password_page.enter_confirm_password("")


@when("user clicks Update button")
def click_update_btn(context):
    change_password_page = context.change_password_page
    change_password_page.click_update_btn()


@then("message \"Password changed successfully\" appears")
def check_success_msg(context):
    browser = context.browser
    change_password_page = context.change_password_page
    change_password_msg = change_password_page.get_general_message()
    assert change_password_msg == "Password changed successfully"
    time.sleep(2)
    browser.shutdown()


@then("message \"Your current password is incorrect, please enter correct password.\" appears")
def check_success_msg(context):
    browser = context.browser
    change_password_page = context.change_password_page
    change_password_msg = change_password_page.get_general_message()
    assert change_password_msg == "Your current password is incorrect, please enter correct password."
    time.sleep(2)
    browser.shutdown()


@then("message \"Passwords do not match\" appears")
def check_not_match_msg(context):
    browser = context.browser
    change_password_page = context.change_password_page
    change_password_msg = change_password_page.get_new_password_message()
    change_confirm_msg = change_password_page.get_confirm_password_message()
    assert change_password_msg == "Passwords do not match"
    assert change_confirm_msg == "Passwords do not match"
    time.sleep(2)
    browser.shutdown()


@then("message \"The password is too short\" appears")
def check_short_password_msg(context):
    browser = context.browser
    change_password_page = context.change_password_page
    change_password_msg = change_password_page.get_new_password_message()
    change_confirm_msg = change_password_page.get_confirm_password_message()
    assert change_password_msg == "The password is too short"
    assert change_confirm_msg == "The password is too short"
    time.sleep(2)
    browser.shutdown()


@then("message \"Password field shouldn’t be empty\" appears")
def check_empty_confirm_msg(context):
    browser = context.browser
    change_password_page = context.change_password_page
    change_password_msg = change_password_page.get_new_password_message()
    change_confirm_msg = change_password_page.get_confirm_password_message()
    assert change_password_msg == "Password field shouldn’t be empty"
    assert change_confirm_msg == "Confirm Password field shouldn’t be empty"
    time.sleep(2)
    browser.shutdown()


@then("message \"Confirm Password field shouldn’t be empty\" appears")
def check_empty_confirm_msg(context):
    browser = context.browser
    change_password_page = context.change_password_page
    change_confirm_msg = change_password_page.get_confirm_password_message()
    assert change_confirm_msg == "Confirm Password field shouldn’t be empty"
    time.sleep(2)
    browser.shutdown()

