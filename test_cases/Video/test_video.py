import pytest
import tests.ui_tests.utils.configs as configs

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.before_we_begin_page import BeforeWeBeginPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage
from tests.ui_tests.pages.privacy_page import PrivacyPage
from tests.ui_tests.pages.digital_interview_page import DigitalInterview
from tests.ui_tests.pages.video_assessment_welcome_page import \
    VideoAssessmentWelcomePage
from tests.ui_tests.pages.games_page import GamesPage
from tests.ui_tests.pages.traits_report_page import TraitsReportPage
from tests.ui_tests.pages.accessibility_settings_page import \
    AccessibilitySettingsPage


@pytest.mark.C912550
@pytest.mark.login
@pytest.mark.video
def test_setup_video_user_not_started_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret('setup_video_user_not_started_web')
    driver.visit('C912550', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    privacy_page = PrivacyPage(driver)
    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    bwb_page = BeforeWeBeginPage(driver)
    bwb_page.click_continue()

    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)
    driver.click(GamesApplicationPage.complete_video_interview_button)
    driver.wait_until_element_visible(
        VideoAssessmentWelcomePage.pymetrics_logo)
    driver.click(VideoAssessmentWelcomePage.continue_button)
    about = driver.return_text(VideoAssessmentWelcomePage.title_header)
    driver.click(VideoAssessmentWelcomePage.close_icon)
    complete_video_text = driver.return_text(
        GamesApplicationPage.complete_video_interview_button
    )
    assert complete_video_text == 'Complete Digital Interview'


@pytest.mark.C914175
@pytest.mark.video
def test_setup_video_games_complete_less_than_1_year_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret('setup_video_games_complete_less_than_1_year_web')
    driver.visit('C914175', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    privacy_page = PrivacyPage(driver)
    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    bwb_page = BeforeWeBeginPage(driver)
    bwb_page.click_continue()

    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)

    driver.return_element(GamesPage.checked_game_cards)
    driver.click(GamesApplicationPage.view_traits_button)
    driver.wait_until_element_visible(TraitsReportPage.breakdown_nav)


@pytest.mark.video
@pytest.mark.smoke
def test_complete_video_steps(driver):
    LoginPage.login(driver, '/login')
    driver.click(GamesApplicationPage.main_complete_video_interview_button)
    continue_button = driver.return_text(
        VideoAssessmentWelcomePage.continue_button
    )
    assert continue_button == 'Continue'
    driver.click(VideoAssessmentWelcomePage.continue_button)
    driver.wait_until_element_visible(VideoAssessmentWelcomePage.role_video)
    driver.click(VideoAssessmentWelcomePage.continue_button)
    driver.wait_until_element_visible(
        VideoAssessmentWelcomePage.expectation_page)
    driver.click(VideoAssessmentWelcomePage.expectation_continue_button)
    driver.wait_until_element_visible(
        VideoAssessmentWelcomePage.test_progress_bar)


@pytest.mark.C914051
@pytest.mark.video
def test_setup_video_games_complete_more_than_1_year_resubmit_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_video_games_complete_more_than_1_year_resubmit_web')
    driver.visit('C914051', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    privacy_page = PrivacyPage(driver)
    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    bwb_page = BeforeWeBeginPage(driver)
    bwb_page.click_continue()

    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)

    driver.click(GamesApplicationPage.application_complete_games_button)
    driver.click(GamesApplicationPage.language_dropdown)
    driver.click(GamesApplicationPage.english_option)
    driver.click(GamesApplicationPage.finish_and_play_games_btn)
    driver.wait_until_element_visible(GamesPage.replay_games)


@pytest.mark.C914058
@pytest.mark.video
def test_setup_video_user_2_positons_2_video_1_game_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_video_user_2_positons_2_video_1_game_web')
    driver.visit('C914058', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    privacy_page = PrivacyPage(driver)
    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    bwb_page = BeforeWeBeginPage(driver)
    bwb_page.click_continue()

    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)
    driver.wait_until_element_visible(
        GamesApplicationPage.application_complete_games_button)
    driver.navigate_to(configs.url + '/applications')
    driver.wait_until_element_visible(
        GamesApplicationPage.main_complete_video_interview_button)
    video_buttons = driver.return_elements(
        GamesApplicationPage.main_complete_video_interview_button)
    complete_game_button = driver.return_elements(
        GamesApplicationPage.action_items_complete_games_button)
    assert len(video_buttons) == 2
    assert len(complete_game_button) == 1


@pytest.mark.video_feedback
@pytest.mark.video
@pytest.mark.interview_completion
def test_complete_video_survey(driver):
    LoginPage.login(driver, '/login')
    driver.wait_until_element_visible(GamesApplicationPage.applications_logo)
    driver.navigate_to(configs.url + '/video/assessment/abf66cf0-245e-4a98-af40-cc54e84fc8b2/feedback') # noqa
    driver.wait_until_element_visible(
        GamesApplicationPage.interview_feedback_page)


@pytest.mark.video_completion
@pytest.mark.video
@pytest.mark.interview_completion
def test_complete_video_screen(driver):
    LoginPage.login(driver, '/login')
    driver.wait_until_element_visible(GamesApplicationPage.applications_logo)
    driver.navigate_to(configs.url + '/video/assessment/abf66cf0-245e-4a98-af40-cc54e84fc8b2/complete') # noqa
    driver.wait_until_element_visible(
        GamesApplicationPage.interview_complete_page)


@pytest.mark.C1246968
@pytest.mark.audio
@pytest.mark.interview_completion
def test_complete_audio_survey(driver):
    LoginPage.login(driver, '/login')
    driver.wait_until_element_visible(GamesApplicationPage.applications_logo)
    driver.navigate_to(configs.url + '/video/assessment/1ecaf16e-f8cc-4731-aa19-53647386a70b/feedback') # noqa
    driver.wait_until_element_visible(
        GamesApplicationPage.interview_feedback_page)


@pytest.mark.C1246969
@pytest.mark.audio
@pytest.mark.interview_completion
def test_complete_audio_screen(driver):
    LoginPage.login(driver, '/login')
    driver.wait_until_element_visible(GamesApplicationPage.applications_logo)
    driver.navigate_to(configs.url + '/video/assessment/1ecaf16e-f8cc-4731-aa19-53647386a70b/complete') # noqa
    driver.wait_until_element_visible(
        GamesApplicationPage.interview_complete_page)


@pytest.mark.video_interview
@pytest.mark.flaky(reruns=2)
@pytest.mark.regression_no_csv
def test_video_interview(driver):
    LoginPage.login_user_no_games(driver, '/login')
    driver.wait_until_element_visible(GamesApplicationPage.applications_logo)
    driver.click(GamesApplicationPage.main_complete_video_interview_button)
    driver.wait_until_element_visible(DigitalInterview.languages_continue)
    driver.click(DigitalInterview.languages_continue)
    driver.click(DigitalInterview.languages_continue)
    driver.wait_until_element_visible(DigitalInterview.main_continue)
    driver.click(DigitalInterview.main_continue)
    driver.wait_until_element_visible(DigitalInterview.company_continue)
    driver.click(DigitalInterview.company_continue)
    driver.wait_until_element_visible(DigitalInterview.what_to_expect_continue)
    driver.click(DigitalInterview.what_to_expect_continue)
    driver.wait_until_element_visible(DigitalInterview.start_tests)
    driver.click(DigitalInterview.start_tests)
    driver.wait_until_element_visible(DigitalInterview.tests_info)


@pytest.mark.audio_interview
@pytest.mark.flaky(reruns=2)
@pytest.mark.regression_no_csv
def test_audio_interview(driver):
    LoginPage.login_user_audio_interview(driver, '/login')
    driver.wait_until_element_visible(GamesApplicationPage.applications_logo)
    driver.click(GamesApplicationPage.main_complete_video_interview_button)
    driver.wait_until_element_visible(DigitalInterview.languages_continue)
    driver.click(DigitalInterview.languages_continue)
    driver.click(DigitalInterview.languages_continue)
    driver.wait_until_element_visible(DigitalInterview.main_continue)
    driver.click(DigitalInterview.main_continue)
    driver.wait_until_element_visible(DigitalInterview.company_continue)
    driver.click(DigitalInterview.company_continue)
    driver.wait_until_element_visible(DigitalInterview.what_to_expect_continue)
    driver.click(DigitalInterview.what_to_expect_continue)
    driver.wait_until_element_visible(DigitalInterview.start_tests)
    driver.click(DigitalInterview.start_tests)
    driver.wait_until_element_visible(DigitalInterview.tests_info)
