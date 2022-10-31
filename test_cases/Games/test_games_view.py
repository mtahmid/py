import pytest
import time

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage
from tests.ui_tests.pages.games_page import GamesPage


import tests.ui_tests.utils.configs as configs


@pytest.mark.game_one
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game1_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    gp = GamesPage(driver)
    time.sleep(1)
    gp.click_games_play_button('1')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'


@pytest.mark.game_two
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game2_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    gp = GamesPage(driver)
    time.sleep(1)
    gp.click_games_play_button('2')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'


@pytest.mark.game_three
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game3_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    gp = GamesPage(driver)
    time.sleep(1)
    gp.click_games_play_button('3')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'


@pytest.mark.game_four
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game4_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    time.sleep(2)
    driver.click(GamesPage.scroll_right_btn)
    gp = GamesPage(driver)
    gp.click_games_play_button('4')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'


@pytest.mark.game_five
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game5_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    time.sleep(2)
    for click in range(2):
        driver.click(GamesPage.scroll_right_btn)
    gp = GamesPage(driver)
    gp.click_games_play_button('5')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'


@pytest.mark.game_six
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game6_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    time.sleep(2)
    for click in range(3):
        driver.click(GamesPage.scroll_right_btn)
    gp = GamesPage(driver)
    gp.click_games_play_button('6')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'


@pytest.mark.game_seven
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game7_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    time.sleep(2)
    for click in range(4):
        driver.click(GamesPage.scroll_right_btn)
    gp = GamesPage(driver)
    gp.click_games_play_button('7')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'


@pytest.mark.game_eight
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game8_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    time.sleep(2)
    for click in range(5):
        driver.click(GamesPage.scroll_right_btn)
    gp = GamesPage(driver)
    gp.click_games_play_button('8')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'


@pytest.mark.game_nine
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game9_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    time.sleep(2)
    for click in range(6):
        driver.click(GamesPage.scroll_right_btn)
    gp = GamesPage(driver)
    gp.click_games_play_button('9')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'


@pytest.mark.game_ten
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game10_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    time.sleep(2)
    for click in range(7):
        driver.click(GamesPage.scroll_right_btn)
    gp = GamesPage(driver)
    gp.click_games_play_button('10')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'


@pytest.mark.game_eleven
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game11_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    time.sleep(2)
    for click in range(8):
        driver.click(GamesPage.scroll_right_btn)
    gp = GamesPage(driver)
    gp.click_games_play_button('11')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'


@pytest.mark.game_twelve
@pytest.mark.games_check
@pytest.mark.smoke
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_game12_appears(driver):
    LoginPage.login(driver, '/login')
    ga = GamesApplicationPage(driver)
    ga.bypass_game_advice()
    time.sleep(2)
    for click in range(9):
        driver.click(GamesPage.scroll_right_btn)
    gp = GamesPage(driver)
    gp.click_games_play_button('12')
    driver.wait_until_element_visible(GamesPage.game_player_iframe)
    driver.switch_frame(GamesPage.iframe)
    time.sleep(1)
    continue_text = driver.return_text(GamesPage.blue_continue_button)
    assert continue_text == 'Continue'
