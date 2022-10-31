import pytest

import tests.ui_tests.utils.configs as configs
from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.register_page import RegisterPage
from tests.ui_tests.pages.before_we_begin_page import BeforeWeBeginPage
from tests.ui_tests.pages.games_page import GamesPage
from tests.ui_tests.pages.welcome_back_page import WelcomeBackPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage
from tests.ui_tests.pages.privacy_page import PrivacyPage

import time

@pytest.mark.csv_secret
@pytest.mark.register
@pytest.mark.C44808
@pytest.mark.assessment_to_run
@pytest.mark.regression
def test_setup_new_user_register_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret('setup_new_user_register_web')
    driver.visit('C44808', secret)

    register_page = RegisterPage(driver).wait_until_page_load()
    assert register_page.get_email_value() != ''

    register_page.set_password(configs.client['password'])
    register_page.set_confirm_password(configs.client['password'])
    driver.click(register_page.language_dropdown)
    driver.click(register_page.english_language_option)
    privacy_page = register_page.click_register_button()
    driver.wait_until_element_visible(PrivacyPage.submit_consent_button)


@pytest.mark.csv_secret
@pytest.mark.register
@pytest.mark.C44809
@pytest.mark.assessment_to_run
@pytest.mark.regression
def test_setup_existing_user_register_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret('setup_existing_user_register_web')
    driver.visit('C44809', secret)

    login_page = LoginPage(driver)
    assert login_page.get_username() == secret['username']


@pytest.mark.csv_secret
@pytest.mark.register
@pytest.mark.C44810
@pytest.mark.assessment_to_run
@pytest.mark.regression
def test_setup_existing_user_completed_games_register_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret('setup_existing_user_completed_games_register_web')
    driver.visit('C44810', secret)
    LoginPage.login_with_given_csv_user(driver, secret['password'])
    driver.wait_until_element_visible(PrivacyPage.submit_consent_button)


@pytest.mark.csv_secret
@pytest.mark.register
@pytest.mark.C44811
@pytest.mark.assessment_to_run
@pytest.mark.regression
def test_setup_existing_user_completed_over_a_year_register_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_existing_user_completed_over_a_year_register_web'
    )
    driver.visit('C44811', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    time.sleep(3)
    privacy_page = PrivacyPage(driver)
    privacy_page.click_consent_all()
    privacy_page.click_consent_all()
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    bwb_page = BeforeWeBeginPage(driver)
    bwb_page.click_continue()

    ga_page = GamesApplicationPage(driver)
    driver.click(GamesApplicationPage.application_complete_games_button)

    driver.wait_until_element_visible(GamesApplicationPage.language_dropdown)
    driver.click(GamesApplicationPage.language_dropdown)
    driver.click(GamesApplicationPage.english_option)
    driver.click(GamesApplicationPage.finish_and_play_games_btn)

    games_page = GamesPage(driver)
    assert games_page.get_title() == 'THE GAMES'
