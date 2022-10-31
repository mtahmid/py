import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.before_we_begin_page import BeforeWeBeginPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage
from tests.ui_tests.pages.traits_report_page import TraitsReportPage


import tests.ui_tests.utils.configs as configs


@pytest.mark.C44823
@pytest.mark.csv_secret
@pytest.mark.traits
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_incomplete_user_traits_web(secretFixture, driverFixture):
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_incomplete_user_traits_web'
    )
    driver.visit('C44823', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    bwb_page = BeforeWeBeginPage(driver)
    driver.wait_until_element_visible(BeforeWeBeginPage.continue_button)
    bwb_page.click_continue()

    driver.wait_until_element_visible(
        GamesApplicationPage.application_complete_games_button)


@pytest.mark.C44824
@pytest.mark.csv_secret
@pytest.mark.traits
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_complete_user_traits_web(secretFixture, driverFixture):
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_complete_user_traits_web'
    )
    driver.visit('C44824', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    bwb_page = BeforeWeBeginPage(driver)
    driver.wait_until_element_visible(BeforeWeBeginPage.continue_button)
    bwb_page.click_continue()

    driver.wait_until_element_visible(GamesApplicationPage.view_traits_button)
    driver.click(GamesApplicationPage.view_traits_button)
    driver.wait_until_element_visible(TraitsReportPage.explainer_card)
