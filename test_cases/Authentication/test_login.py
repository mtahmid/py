import os
import pytest
import time

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.welcome_back_page import WelcomeBackPage
from tests.ui_tests.pages.before_we_begin_page import BeforeWeBeginPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage
from tests.ui_tests.pages.games_page import GamesPage
from tests.ui_tests.pages.games_config_page import GamesConfigPage
from tests.ui_tests.pages.privacy_page import PrivacyPage
from tests.ui_tests.pages.settings_page import SettingsPage
from tests.ui_tests.pages.client_portal.dashboard import Dashboard
from tests.ui_tests.pages.traits_report_page import TraitsReportPage
from tests.ui_tests.pages.accessibility_settings_page \
    import AccessibilitySettingsPage


import tests.ui_tests.utils.configs as configs


@pytest.mark.csv_secret
@pytest.mark.login
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_existing_user_completed_games_over_a_year_1_login_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_existing_user_completed_games_over_a_year_1_login_web'
    )
    driver.visit('C44812', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    driver.click(BeforeWeBeginPage.continue_button)
    driver.click(GamesApplicationPage.application_complete_games_button)
    driver.click(GamesApplicationPage.language_dropdown)
    driver.click(GamesApplicationPage.english_option)
    driver.click(GamesApplicationPage.finish_and_play_games_btn)
    driver.wait_until_element_visible(GamesApplicationPage.resubmit_button)
    driver.click(GamesApplicationPage.resubmit_button)
    driver.click(GamesApplicationPage.back_to_application)
    driver.click(GamesApplicationPage.view_results)
    driver.wait_until_element_visible(TraitsReportPage.explainer_card)


@pytest.mark.csv_secret
@pytest.mark.login
@pytest.mark.C44813
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_existing_user_completed_games_over_a_year_2_login_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_existing_user_completed_games_over_a_year_2_login_web'
    )
    driver.visit('C44813', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    driver.click(BeforeWeBeginPage.continue_button)

    driver.click(GamesApplicationPage.application_complete_games_button)
    driver.click(GamesApplicationPage.language_dropdown)
    driver.click(GamesApplicationPage.english_option)
    driver.click(GamesApplicationPage.finish_and_play_games_btn)
    driver.wait_until_element_visible(GamesApplicationPage.replay_games)
    driver.click(GamesApplicationPage.replay_games)
    games_completed_text = driver.return_text(
        GamesPage.completed_games_header_text)
    assert games_completed_text == '0 out of 12 complete'


@pytest.mark.login
@pytest.mark.login_no_games
@pytest.mark.assessment
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_login_no_games(driver):
    LoginPage.login_user_no_games(driver, '/login')
    driver.click(GamesApplicationPage.action_items_complete_games_button)
    games_completed_text = driver.return_text(
        GamesPage.completed_games_header_text)
    assert games_completed_text == '0 out of 12 complete'


@pytest.mark.login
@pytest.mark.ma_login_no_games
@pytest.mark.assessment
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_ma_login_no_games(driver):
    LoginPage.login_ma_user_no_games(driver, '/login')
    driver.click(GamesApplicationPage.action_items_complete_games_button)
    games_completed_text = driver.return_text(
        GamesPage.completed_games_header_text)
    assert games_completed_text == '0 out of 12 complete'


@pytest.mark.login
@pytest.mark.login_started_games
@pytest.mark.assessment
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_login_started_games(driver):
    LoginPage.login_user_started_games(driver, '/applications/321894/games/')
    driver.wait_until_element_visible(GamesPage.completed_games_header_text, delay=120)
    games_completed_text = driver.return_text(
        GamesPage.completed_games_header_text)
    assert games_completed_text == '4 out of 12 complete'


@pytest.mark.login
@pytest.mark.ma_login_started_games
@pytest.mark.assessment
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_ma_login_started_games(driver):
    LoginPage.login_ma_user_started_games(driver, '/applications/335731/games/')
    driver.wait_until_element_visible(GamesPage.completed_games_header_text, delay=120)
    games_completed_text = driver.return_text(
        GamesPage.completed_games_header_text)
    assert games_completed_text == '1 out of 12 complete'


@pytest.mark.login
@pytest.mark.login_completed_games
@pytest.mark.assessment
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_login_completed_games(driver):
    LoginPage.login_user_finished_games(driver, '/applications/323660/')
    driver.wait_until_element_visible(GamesApplicationPage.view_results)


@pytest.mark.login
@pytest.mark.ma_login_completed_games
@pytest.mark.assessment
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_ma_login_completed_games(driver):
    LoginPage.login_ma_user_finished_games(driver, '/applications/341368/')
    driver.wait_until_element_visible(GamesApplicationPage.view_results)


@pytest.mark.csv_secret
@pytest.mark.xfail
@pytest.mark.login
@pytest.mark.C479472
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_user_with_game_replay(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret('setup_user_with_game_replay')
    driver.visit('C479472', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])
    privacy_page = PrivacyPage(driver)
    time.sleep(1)
    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    privacy_page = PrivacyPage(driver)
    privacy_page.click_next_button()
    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    driver.click(GamesApplicationPage.application_complete_games_button)
    driver.click(GamesApplicationPage.language_dropdown)
    driver.click(GamesApplicationPage.english_option)
    driver.click(GamesApplicationPage.finish_and_play_games_btn)

    driver.click(GamesApplicationPage.next_step_complete_games_button)
    driver.click(GamesConfigPage.submit_button)

    driver.click(GamesApplicationPage.resubmit_button)
    time.sleep(2)

    games_completed_text = driver.return_text(
        GamesPage.completed_games_header_text)
    assert games_completed_text == '0 out of 3 complete'


@pytest.mark.C123
@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.production
@pytest.mark.login
@pytest.mark.assessment
@pytest.mark.regression
def test_basic_login(driver):
    driver.navigate_to(configs.url + '/login')
    driver.type_keys(LoginPage.userNameTextBox, os.environ['UI_LOGIN_USER'])
    driver.type_keys(LoginPage.passwordTextBox,
                     os.environ['UI_LOGIN_PASSWORD'])
    driver.click(LoginPage.submitButton)
    driver.wait_until_element_visible(SettingsPage.account_dropdown)


@pytest.mark.C898313
@pytest.mark.login
@pytest.mark.client_portal
@pytest.mark.assessment
@pytest.mark.regression
def test_client_portal_login(driver):
    LoginPage.login_recruiter(driver, '/c/p')
    driver.wait_until_element_visible(Dashboard.high_chart)


@pytest.mark.C739238
@pytest.mark.xfail
@pytest.mark.login
@pytest.mark.replay
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_user_with_game_resubmit(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret('setup_user_with_game_resubmit')
    driver.visit('C739238', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])
    privacy_page = PrivacyPage(driver)
    time.sleep(1)

    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    bwb_page = BeforeWeBeginPage(driver)
    assert bwb_page.get_title() == 'BEFORE WE BEGIN...'
    bwb_page.click_continue()

    driver.click(GamesApplicationPage.complete_games_button)
    driver.click(GamesConfigPage.submit_button)

    driver.click(GamesPage.games_info_popup_close)
    time.sleep(2)
    driver.click(GamesApplicationPage.resubmit_button)
    driver.click(GamesApplicationPage.back_to_application)
    driver.click(GamesApplicationPage.view_results)
    driver.wait_until_element_visible(TraitsReportPage.explainer_card)


@pytest.mark.C739240
@pytest.mark.login
@pytest.mark.replay
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_incomplete_user_finished_nr_games(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret('setup_incomplete_user_finished_nr_games')
    driver.visit('C739240', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    privacy_page = PrivacyPage(driver)
    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    driver.wait_until_element_visible(BeforeWeBeginPage.continue_button)
    driver.click(BeforeWeBeginPage.continue_button)

    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)
    driver.click(GamesApplicationPage.application_complete_games_button)
    driver.click(GamesApplicationPage.language_dropdown)
    driver.click(GamesApplicationPage.english_option)
    driver.click(GamesApplicationPage.finish_and_play_games_btn)
    driver.click(GamesApplicationPage.games_close_icon)
    games_completed_text = driver.return_text(
        GamesPage.completed_games_header_text)
    assert games_completed_text == '5 out of 17 complete'


@pytest.mark.C739241
@pytest.mark.login
@pytest.mark.replay
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_complete_user_no_game_replay(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret('setup_complete_user_no_game_replay')
    driver.visit('C739241', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    privacy_page = PrivacyPage(driver)
    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    driver.click(BeforeWeBeginPage.continue_button)

    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)

    driver.return_element(GamesApplicationPage.checked_games_circle)
    view_traits = driver.return_text(GamesApplicationPage.view_traits_button)
    assert view_traits == 'View Results'
    driver.click(GamesApplicationPage.view_traits_button)
    driver.wait_until_element_visible(
        TraitsReportPage.explainer_card)


@pytest.mark.C914057
@pytest.mark.login
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_video_new_user_invited_to_both_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret('setup_video_new_user_invited_to_both_web')
    driver.visit('C914057', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    privacy_page = PrivacyPage(driver)
    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    driver.wait_until_element_visible(BeforeWeBeginPage.continue_button)
    driver.click(BeforeWeBeginPage.continue_button)

    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)
    driver.wait_until_element_visible(
        GamesApplicationPage.application_complete_games_button)
    driver.navigate_to(configs.url + '/applications')
    driver.wait_until_element_visible(
        GamesApplicationPage.action_items_complete_games_button)
    driver.wait_until_element_visible(
        GamesApplicationPage.main_complete_video_interview_button)


@pytest.mark.C914050
@pytest.mark.login
@pytest.mark.assessment
@pytest.mark.regression
def test_setup_video_games_complete_more_than_1_year_replay_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_video_games_complete_more_than_1_year_replay_web')
    driver.visit('C914050', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    privacy_page = PrivacyPage(driver)
    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    driver.wait_until_element_visible(BeforeWeBeginPage.continue_button)
    driver.click(BeforeWeBeginPage.continue_button)

    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)
    driver.wait_until_element_visible(
        GamesApplicationPage.application_complete_games_button)
    driver.click(GamesApplicationPage.application_complete_games_button)
    driver.click(GamesApplicationPage.language_dropdown)
    driver.click(GamesApplicationPage.english_option)
    driver.click(GamesApplicationPage.finish_and_play_games_btn)
    driver.wait_until_element_visible(GamesPage.replay_games)
    driver.click(GamesPage.replay_games)
    games_completed_text = driver.return_text(
        GamesPage.completed_games_header_text)
    assert games_completed_text == '0 out of 12 complete'
