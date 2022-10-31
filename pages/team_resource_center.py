from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.login_page import LoginPage

import tests.ui_tests.utils.configs as configs


class Trc(BasePage):
    my_team = {
        'description': 'My team header',
        'selector': '#header-nav-myteam',
    }
    subtext = {
        'description': 'The text under the main header',
        'selector': '//h2[text() = "Elevate coaching for your team members"]',
        'type': 'xpath',
    }
    main_header = {
        'description': 'Dashboard text',
        'selector': '//h1[text() = "Team Resource Center"]',
        'type': 'xpath',
    }

    def login_trc_user(driver, path):
        """
        :param path: given url path (e.g. /settings, /applications)
        """
        driver.navigate_to(configs.url + path)
        driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+308@pymetrics.com")
        driver.click(LoginPage.next_button)
        driver.type_keys(LoginPage.passwordTextBox, "6428531Vbycr!")
        driver.click(LoginPage.client_portal_login_button)