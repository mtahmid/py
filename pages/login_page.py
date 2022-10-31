import os
import tests.ui_tests.utils.configs as configs

from tests.ui_tests.pages.base_page import BasePage

import time

client_portal_user_name = os.environ['UI_CLIENT_PORTAL_USER']
client_portal_password = os.environ['UI_CLIENT_PORTAL_PASSWORD']
user_name = os.environ['UI_LOGIN_USER']
password = os.environ['UI_LOGIN_PASSWORD']


class LoginPage(BasePage):
    loginTab = {
        'description': 'Login tab on homepage',
        'selector': '//a[@href="/login/"]',
        'type': 'xpath'
    }
    userNameTextBox = {
        'description': 'Login Username textbox',
        'selector': 'username',
        'type': 'name'
    }
    passwordTextBox = {
        'description': 'Password textbox',
        'selector': 'password',
        'type': 'name'
    }
    submitButton = {
        'description': 'Login Submit button',
        'selector': '#login-submit',
        'type': 'css'
    }
    next_button = {
        'description': 'Next button under login page',
        'selector': '#login-init'
    }
    gamesInfoPopup = {
        'description': 'Games info popup',
        'selector': '//div[@data-remodal-id="games-info"]',
        'type': 'xpath'
    }
    pymetricsLogo = {
        'description': 'Pymetrics logo on login page',
        'selector': '.self-end.logo'
    }
    client_portal_login_button = {
        'description': 'Client Portal login button',
        'selector': '[type="submit"]'
    }
    password_reset_link = {
        'description': 'Password reset link',
        'selector': '[href="/auth/password_reset"]'
    }
    forgot_your_password_title = {
        'description': 'Forgot your password title',
        'selector': '.flex-2.regular-font.center-align.watermelon'
    }

    def get_username(self):
        self.driver.take_screenshot()
        return self.driver.return_attribute(self.userNameTextBox, 'value')

    def login_with_given_csv_user(driver, password):
        driver.type_keys(LoginPage.passwordTextBox, password)
        driver.wait_until_element_visible(LoginPage.submitButton)
        driver.click(LoginPage.submitButton)

    def login_without_given_csv_user(driver, user, password):
        driver.type_keys(LoginPage.userNameTextBox, user)
        driver.type_keys(LoginPage.passwordTextBox, password)
        driver.wait_until_element_visible(LoginPage.submitButton)
        driver.click(LoginPage.submitButton)

    def wait_until_page_load(self):
        self.driver.wait_until_element_visible(self.pymetricsLogo)
        self.driver.add_metadata_cookie()
        return self

    def login(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, user_name)
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, password)
        driver.click(LoginPage.submitButton)

    def login_recruiter(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, client_portal_user_name)
        driver.type_keys(LoginPage.passwordTextBox, client_portal_password)
        driver.click(LoginPage.client_portal_login_button)

    def login_dev_report_contributor(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+inc184@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "6428531Vbycr!")
        driver.click(LoginPage.client_portal_login_button)

    def login_dev_report_leadership(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+inc186@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "6428531Vbycr!")
        driver.click(LoginPage.client_portal_login_button)

    def login_user_no_games(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+638@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "6428531Vbycr!")
        driver.click(LoginPage.client_portal_login_button)

    def login_user_started_games(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+620@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "6428531Vbycr!")
        driver.click(LoginPage.client_portal_login_button)

    def login_user_finished_games(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+641@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "6428531Vbycr!")
        driver.click(LoginPage.client_portal_login_button)


    def login_user_audio_interview(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+and95@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "6428531Vbycr!")
        driver.click(LoginPage.client_portal_login_button)


    def login_user_marketplace(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+market1@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "Tiffany0916!")
        driver.click(LoginPage.client_portal_login_button)

    def cp_member(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+member@pymetrics.com")
        driver.type_keys(LoginPage.passwordTextBox, "6428531_Vbycr")
        driver.click(LoginPage.client_portal_login_button)

    def login_ma_user_no_games(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+712@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "6428531Vbycr!")
        driver.click(LoginPage.client_portal_login_button)

    def login_ma_user_started_games(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+686@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "6428531Vbycr!")
        driver.click(LoginPage.client_portal_login_button)

    def login_ma_user_finished_games(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+730@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "6428531_Vbycr")
        driver.click(LoginPage.client_portal_login_button)

    def login_spanish_user(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+732@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "6428531Vbycr!")
        driver.click(LoginPage.client_portal_login_button)
