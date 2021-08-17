from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class Browser:
    """
    This class is wrapper around Selenium driver
    """
    # Exercise  # 1
    # Add to Browser 's initialization method an exception handling that will print out
    # the executable path to the driver is incorrect
    def __init__(self, url, browser_name="", time_wait=10):
        # decide which browser to open, can be extended
        try:
            if browser_name.lower() == 'firefox':
                self.driver = webdriver.Firefox(executable_path='../../drivers/geckodriver')
            elif browser_name.lower() == 'chrome':
                options = webdriver.ChromeOptions()
                options.add_argument("--start-maximized")
                self.driver = webdriver.Chrome(executable_path='../../drivers/chromedriver', options=options)
                # self.driver = webdriver.Chrome(executable_path='drivers/chromedriver', desired_capabilities={"chromeOptions": {"binary": 'mycefapp.exe'}})
            elif browser_name.lower() == 'remote':
                BROWSERSTACK_URL = 'https://mameluke_wLf8hY:qzjc5gmzzRX3vUKEASnm@hub-cloud.browserstack.com/wd/hub'
                desired_cap = {
                    'os_version': 'Big Sur',
                    'resolution': '1920x1080',
                    'browser': 'Chrome',
                    'browser_version': '90',
                    'os': 'OS X',
                    'name': "svetlanamatcheny1's Why Telvero Test Big Sur"
                }
                self.driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)

                # username = "mameluke_wLf8hY"
                # accessKey = "qzjc5gmzzRX3vUKEASnm"
                # desired_cap = {
                #     'os_version': 'Catalina',
                #      'os': 'OS X',
                #     'browser': 'firefox',
                #     'browser_version': '86.0',
                #     'name': 'Parallel Test1', # test name
                #     'build': 'browserstack-build-1', # Your tests will be organized within this build
                #     'acceptSslCerts': 'true'
                #                }
                # self.driver = webdriver.Remote(
                #     command_executor='https://' + username + ':' + accessKey + '@hub-cloud.browserstack.com/wd/hub',
                #     desired_capabilities=desired_cap)

        except WebDriverException as err:
            print("Incorrect path to WebDriver:", err)
            raise

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(time_wait)

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()
