import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.settings_page import SettingsPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage

import tests.ui_tests.utils.configs as configs


@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.production
@pytest.mark.assessment
@pytest.mark.regression
def test_logout(driver):
    LoginPage.login(driver, '/login')
    driver.click(SettingsPage.account_dropdown)
    driver.click(GamesApplicationPage.dropdown_logout)
    driver.return_element(LoginPage.userNameTextBox)
