import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.client_portal.privacy import Privacy
from tests.ui_tests.pages.client_portal.dashboard import Dashboard

import tests.ui_tests.utils.configs as configs


@pytest.mark.cp_privacy
@pytest.mark.client_portal
def test_privacy_button(driver):
    LoginPage.login_recruiter(driver, '/c/p')
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + '/privacy/account/')
    driver.wait_until_element_visible(Privacy.delete_account_button)
