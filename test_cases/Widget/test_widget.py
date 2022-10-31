import os
import pytest

import tests.ui_tests.utils.configs as configs
from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.widget_page import WidgetPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage

user = os.environ['UI_LOGIN_USER']
password = os.environ['UI_LOGIN_PASSWORD']


@pytest.mark.xfail  # can't get passed the skills section for onboarding
@pytest.mark.C886057
@pytest.mark.widget
@pytest.mark.smoke
def test_applications_help_tab(driver):
    driver.navigate_to(configs.url + '/embeddable/widget/6')
    driver.click(WidgetPage.login_button)
    driver.type_keys(LoginPage.userNameTextBox, user)
    driver.type_keys(LoginPage.passwordTextBox, password)
    driver.click(LoginPage.submitButton)
    driver.click(GamesApplicationPage.help_tab)
    driver.wait_until_element_visible(GamesApplicationPage.help_header)
    help_header = driver.return_text(GamesApplicationPage.help_header)
    assert help_header == 'HELP'


@pytest.mark.widget
@pytest.mark.smoke
def test_widget_30(driver):
    driver.navigate_to(configs.url + '/embeddable/widget/30')
    driver.wait_until_element_visible(WidgetPage.widget_auth_page)
