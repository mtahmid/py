import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.team_resource_center import Trc
from tests.ui_tests.pages.games_application_page import GamesApplicationPage


@pytest.mark.trc_login
@pytest.mark.team_resource_center
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_trc_login(driver):
    Trc.login_trc_user(driver, '/login')
    driver.wait_until_element_visible(Trc.my_team)
    driver.click(Trc.my_team)
    driver.wait_until_element_visible(Trc.subtext)
    driver.wait_until_element_visible(Trc.main_header)


@pytest.mark.trc_login_no_access
@pytest.mark.team_resource_center
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_trc_login_no_access(driver):
    LoginPage.login_user_started_games(driver, '/team-resource-center')
    driver.wait_until_element_visible(GamesApplicationPage.dashboard_text)
