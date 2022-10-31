import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.settings_page import SettingsPage


@pytest.mark.change_email
@pytest.mark.production
@pytest.mark.settings
@pytest.mark.regression_no_csv
def test_settings_change_email(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.change_email_button)
    driver.wait_until_element_visible(SettingsPage.email_update_modal_text)
