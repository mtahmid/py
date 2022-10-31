import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.before_we_begin_page import BeforeWeBeginPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage
from tests.ui_tests.pages.games_page import GamesPage
from tests.ui_tests.pages.accessibility_settings_page \
    import AccessibilitySettingsPage

import tests.ui_tests.utils.configs as configs


@pytest.mark.csv_secret
@pytest.mark.assessment
@pytest.mark.accessibility
@pytest.mark.C44819
@pytest.mark.regression
def test_setup_user_1_accessibility_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_user_1_accessibility_web'
    )
    driver.visit('C44819', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    bwb_page = BeforeWeBeginPage(driver)
    bwb_page.click_continue()

    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)

    ga_page = GamesApplicationPage(driver)
    ga_page.get_to_the_games()

    the_games = driver.return_text(GamesPage.title)
    assert the_games == 'THE GAMES'


@pytest.mark.csv_secret
@pytest.mark.assessment
@pytest.mark.accessibility
@pytest.mark.C44820
@pytest.mark.regression
def test_setup_user_2_accessibility_web(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_user_2_accessibility_web'
    )
    driver.visit('C44820', secret)

    LoginPage.login_with_given_csv_user(driver, secret['password'])

    bwb_page = BeforeWeBeginPage(driver)
    bwb_page.click_continue()

    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)

    ga_page = GamesApplicationPage(driver)
    ga_page.get_to_the_games()

    the_games = driver.return_text(GamesPage.title)
    assert the_games == 'THE GAMES'
