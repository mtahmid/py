import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.before_we_begin_page import BeforeWeBeginPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage
from tests.ui_tests.pages.games_page import GamesPage
from tests.ui_tests.pages.Games.faces import Faces
from tests.ui_tests.pages.privacy_page import PrivacyPage
from tests.ui_tests.pages.accessibility_settings_page \
    import AccessibilitySettingsPage


@pytest.mark.csv_secret
@pytest.mark.games
@pytest.mark.C912470
def test_setup_games_completed_11_games_games_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_games_completed_11_games_games_web'
    )
    driver.visit('C912470', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    bwb_page = BeforeWeBeginPage(driver)
    bwb_page.click_continue()
    ga_page = GamesApplicationPage(driver)
    ga_page.lets_get_to_the_games()
    driver.click(GamesApplicationPage.games_close_icon)
    title = driver.return_text(GamesApplicationPage.completion_title)
    assert title == '11 out of 12 complete'


@pytest.mark.csv_secret
@pytest.mark.games
@pytest.mark.C912469
def test_setup_games_completed_zero_games_games_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_games_completed_zero_games_games_web'
    )
    driver.visit('C912469', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    bwb_page = BeforeWeBeginPage(driver)
    bwb_page.click_continue()
    ga_page = GamesApplicationPage(driver)
    ga_page.lets_get_to_the_games()
    driver.wait_until_element_visible(GamesApplicationPage.i_understand_btn)
    driver.click(GamesApplicationPage.i_understand_btn)
    driver.click(GamesApplicationPage.games_close_icon)
    assert ga_page.get_completion_title() == '0 out of 12 complete'


@pytest.mark.games
@pytest.mark.smoke
@pytest.mark.C898317
@pytest.mark.production
def test_game_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    the_games = driver.return_text(GamesPage.title)
    assert the_games == 'THE GAMES'


@pytest.mark.csv_secret
@pytest.mark.games
@pytest.mark.C739239
def test_setup_user_no_game_replay(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_user_no_game_replay'
    )
    driver.visit('C739239', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    privacy_page = PrivacyPage(driver)
    driver.wait_until_element_visible(privacy_page.consent_all_checkbox)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()

    driver.wait_until_element_visible(BeforeWeBeginPage.continue_button)
    driver.click(BeforeWeBeginPage.continue_button)

    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)
    driver.click(GamesApplicationPage.no_game_replay_complete_games_button)
    driver.click(GamesApplicationPage.language_dropdown)
    driver.click(GamesApplicationPage.english_option)
    driver.click(GamesApplicationPage.finish_and_play_games_btn)
    driver.wait_until_element_visible(GamesApplicationPage.i_understand_btn)
    driver.click(GamesApplicationPage.i_understand_btn)
    driver.click(GamesApplicationPage.games_close_icon)
    games_completed_text = driver.return_text(
        GamesPage.completed_games_header_text)
    assert games_completed_text == '0 out of 3 complete'
