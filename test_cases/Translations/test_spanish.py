import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.Translations.spanish import Spanish
from tests.ui_tests.pages.games_page import GamesPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage
from tests.ui_tests.pages.digital_interview_page import DigitalInterview

from selenium.webdriver.common.by import By


@pytest.mark.money_exchange_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_money_exchange_spanish(driver):
    Spanish.getting_to_games(driver)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[0].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.money_exchange_instructions_in_spanish)
    driver.wait_until_element_visible(Spanish.continue_in_spanish)
    driver.click(Spanish.continue_in_spanish)
    driver.click(Spanish.begin_in_spanish)
    driver.wait_until_element_visible(Spanish.euro_symbol)
    driver.wait_until_element_visible(Spanish.euros_amount)
    driver.wait_until_element_visible(Spanish.game1_title)


@pytest.mark.keypress_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_keypress_spanish(driver):
    Spanish.getting_to_games(driver)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[1].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.keypress_instructions_in_spanish)
    driver.wait_until_element_visible(Spanish.keypress_game_space_bar)
    driver.wait_until_element_visible(Spanish.continue_in_spanish)
    driver.click(Spanish.continue_in_spanish)
    driver.wait_until_element_visible(Spanish.left_hand)


@pytest.mark.balloons_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_balloons_spanish(driver):
    Spanish.getting_to_games(driver)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[2].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.another_euro_symbol)
    driver.wait_until_element_visible(Spanish.balloons_instructions_in_spanish)
    driver.click(Spanish.continue_in_spanish)
    driver.click(Spanish.begin_in_spanish)
    driver.wait_until_element_visible(Spanish.balloons_pump)


@pytest.mark.money_exchange2_game_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_money_exchange2_game_spanish(driver):
    Spanish.getting_to_games(driver)
    driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[3].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.money_exchange2_instructions_in_spanish)
    driver.click(Spanish.continue_in_spanish)
    driver.click(Spanish.begin_in_spanish)
    driver.wait_until_element_visible(Spanish.money_exchange2_text)
    driver.wait_until_element_visible(Spanish.euro_symbol)


@pytest.mark.digits_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_digits_spanish(driver):
    Spanish.getting_to_games(driver)
    for click in range(2):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[4].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.digits_game_instructions_in_spanish)
    driver.click(Spanish.continue_in_spanish)
    driver.click(Spanish.begin_in_spanish)
    driver.wait_until_element_visible(Spanish.digits_game_text)


@pytest.mark.easy_or_hard_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_easy_or_hard_spanish(driver):
    Spanish.getting_to_games(driver)
    for click in range(3):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[5].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.easy_or_hard_instructions_in_spanish)
    driver.wait_until_element_visible(Spanish.another_euro_symbol)
    driver.click(Spanish.continue_in_spanish)
    driver.click(Spanish.begin_in_spanish)
    driver.wait_until_element_visible(Spanish.easy_or_hard_text)


@pytest.mark.stop_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_stop_spanish(driver):
    Spanish.getting_to_games(driver)
    for click in range(4):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[6].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.stop_instructions_in_spanish)


@pytest.mark.cards_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_cards_spanish(driver):
    Spanish.getting_to_games(driver)
    for click in range(5):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[7].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.cards_instructions_in_spanish)
    driver.click(Spanish.continue_in_spanish)
    driver.click(Spanish.begin_in_spanish)
    driver.wait_until_element_visible(Spanish.cards_text)
    driver.wait_until_element_visible(Spanish.another_euro_symbol)


@pytest.mark.arrows_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_arrows_spanish(driver):
    Spanish.getting_to_games(driver)
    for click in range(6):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[8].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.arrows_instructions_in_spanish)


@pytest.mark.length_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_length_spanish(driver):
    Spanish.getting_to_games(driver)
    for click in range(7):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[9].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.length_instructions_in_spanish)
    driver.click(Spanish.continue_in_spanish)
    driver.click(Spanish.begin_in_spanish)
    driver.wait_until_element_visible(Spanish.another_euro_symbol)


@pytest.mark.towers_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_towers_spanish(driver):
    Spanish.getting_to_games(driver)
    for click in range(8):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[10].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.towers_instructions_in_spanish)
    driver.click(Spanish.continue_in_spanish)
    driver.click(Spanish.begin_in_spanish)
    driver.wait_until_element_visible(Spanish.towers_text)


@pytest.mark.faces_game_spanish
@pytest.mark.spanish
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_faces_game_spanish(driver):
    Spanish.getting_to_games(driver)
    for click in range(9):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Spanish.play_games_buttons['selector'])
    play[11].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Spanish.faces_game_instructions_in_spanish)
    driver.click(Spanish.continue_in_spanish)
    driver.click(Spanish.begin_in_spanish)
    driver.wait_until_element_visible(Spanish.faces_game_text)


@pytest.mark.video_interview_spanish
@pytest.mark.flaky(reruns=2)
@pytest.mark.regression_no_csv
def test_video_interview_spanish(driver):
    LoginPage.login_spanish_user(driver, '/login')
    driver.wait_until_element_visible(GamesApplicationPage.applications_logo)
    driver.click(GamesApplicationPage.main_complete_video_interview_button)
    driver.wait_until_element_visible(Spanish.select_dropdown_interview)
    driver.click(Spanish.select_dropdown_interview)
    driver.click(Spanish.spanish_option_interview)
    driver.click(Spanish.select_dropdown_interview)
    driver.click(DigitalInterview.languages_continue)
    driver.wait_until_element_visible(Spanish.configuration_popup)
    driver.click(DigitalInterview.languages_continue)
    driver.wait_until_element_visible(Spanish.intro_text)
    driver.wait_until_element_visible(Spanish.introduction_title_in_spanish)
    driver.click(Spanish.continue_in_spanish_interview)
    driver.wait_until_element_visible(Spanish.about_company_in_spanish)
    driver.click(Spanish.continue_in_spanish_interview)
    driver.wait_until_element_visible(Spanish.what_to_expect)
    driver.wait_until_element_visible(Spanish.min_spanish)
    driver.wait_until_element_visible(Spanish.emphasis_text)
    driver.click(Spanish.continue_in_spanish_interview)
    driver.wait_until_element_visible(Spanish.setup_text)
    driver.click(Spanish.start_tests_interview)
    driver.wait_until_element_visible(Spanish.config_text)
