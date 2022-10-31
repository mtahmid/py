import pytest
import time

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.privacy_page import PrivacyPage
from tests.ui_tests.pages.before_we_begin_page import BeforeWeBeginPage

import tests.ui_tests.utils.configs as configs


@pytest.mark.C44817
@pytest.mark.csv_secret
@pytest.mark.privacy
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_active_membership_user(secretFixture, driverFixture):
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_active_membership_user'
    )
    driver.visit('C44817', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    privacy_page = PrivacyPage(driver)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    driver.wait_until_element_visible(BeforeWeBeginPage.continue_button)


@pytest.mark.C44818
@pytest.mark.csv_secret
@pytest.mark.privacy
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_no_active_membership_user(secretFixture, driverFixture):
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_no_active_membership_user'
    )
    driver.visit('C44818', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    privacy_page = PrivacyPage(driver)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    driver.wait_until_element_visible(BeforeWeBeginPage.continue_button)
