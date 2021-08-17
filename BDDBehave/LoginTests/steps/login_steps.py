from behave import given, when, then
import time

import sys
from os.path import abspath
sys.path.append(abspath('../../../'))

from Telvero.webelements.browser import Browser
from Telvero.utils.config_reader import ConfigReader
from Telvero.pages.login_page import LoginPage
from Telvero.pages.home_page import HomePage
from Telvero.components.settings_left_menu import SettingsLeftMenu
from Telvero.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

URL = "https://www.telvero.com/"
configs = ConfigReader("config.ini")


@given("registered user who is not logged in has home page opened in a browser")
def launch_home_page(context):
    browser = Browser(URL, configs.get_browser('environment'), configs.get_wait_time('environment'))
    context.browser = browser
    home_page = HomePage(browser)
    context.home_page = home_page


@given("user clicks Login button on home page")
def launch_login_page(context):
    home_page = context.home_page
    home_page.open_login_page()


@when("user enters correct both email address and password in the corresponding fields")
def enter_correct_credentials(context):
    browser = context.browser
    driver = browser.get_driver()

    # switching to a new tab
    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    # filling email and password fields on login page
    login_page = LoginPage(browser)
    context.login_page = login_page
    login_page.enter_email_field(configs.get_email('user1'))
    login_page.enter_pass_field(configs.get_password('user1'))


@when("user clicks Sign In button")
def click_login_btn(context):
    login_page = context.login_page
    login_page.click_sign_in_btn()


@then("user account page is open")
def open_account_page(context):
    browser = context.browser
    left_menu = SettingsLeftMenu(browser)
    context.left_menu = left_menu
    left_menu.settings_btn.wait_until_visible()
    time.sleep(2)
    browser.shutdown()
