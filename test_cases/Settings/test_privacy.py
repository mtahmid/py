import pytest
import time
import os

import tests.ui_tests.utils.configs as configs
from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.settings_page import SettingsPage
from tests.ui_tests.pages.privacy_page import PrivacyPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage


@pytest.mark.C898322
@pytest.mark.settings
@pytest.mark.regression
@pytest.mark.regression_no_csv
def test_settings_privacy_notice(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.privacy_nav)
    driver.click(SettingsPage.view_privacy_notice_btn)
    driver.wait_until_element_visible(PrivacyPage.consent_all_checkbox)


@pytest.mark.data_privacy
@pytest.mark.settings
@pytest.mark.regression
@pytest.mark.regression_no_csv
def test_data_privacy(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.data_privacy)
    driver.click(SettingsPage.request_data)
    driver.wait_until_element_visible(SettingsPage.download_data)
    driver.click(SettingsPage.download_data)
    # Commented everything below for future reference
    # time.sleep(1)
    # # Some time for download
    # assert os.path.exists(os.getcwd() +
    #                       '/downloads/PyMetrics.json')
    # os.remove(os.getcwd() + '/downloads/PyMetrics.json')
