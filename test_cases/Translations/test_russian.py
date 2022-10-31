import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.Translations.russian import Russian
from tests.ui_tests.pages.games_page import GamesPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage
from tests.ui_tests.pages.digital_interview_page import DigitalInterview

from selenium.webdriver.common.by import By


@pytest.mark.money_exchange_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_money_exchange_russian(driver):
    Russian.getting_to_games(driver)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[0].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.money_exchange_instructions_in_russian)
    driver.wait_until_element_visible(Russian.continue_in_russian)
    driver.click(Russian.continue_in_russian)
    driver.click(Russian.begin_in_russian)
    driver.wait_until_element_visible(Russian.ruble_symbol)
    driver.wait_until_element_visible(Russian.ruble_amount)
    driver.wait_until_element_visible(Russian.game1_title)


@pytest.mark.keypress_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_keypress_russian(driver):
    Russian.getting_to_games(driver)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[1].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.keypress_instructions_in_russian)
    driver.wait_until_element_visible(Russian.keypress_game_space_bar)
    driver.wait_until_element_visible(Russian.continue_in_russian)
    driver.click(Russian.continue_in_russian)
    driver.wait_until_element_visible(Russian.left_hand)


@pytest.mark.balloons_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_balloons_russian(driver):
    Russian.getting_to_games(driver)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[2].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.another_ruble_symbol)
    driver.wait_until_element_visible(Russian.ballons_instructions_in_russian)
    driver.click(Russian.continue_in_russian)
    driver.click(Russian.begin_in_russian)
    driver.wait_until_element_visible(Russian.balloons_pump)


@pytest.mark.money_exchange2_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_money_exchange2_russian(driver):
    Russian.getting_to_games(driver)
    driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[3].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.money_exchange2_instructions_in_russian)
    driver.click(Russian.continue_in_russian)
    driver.click(Russian.begin_in_russian)
    driver.wait_until_element_visible(Russian.money_exchange2_text)
    driver.wait_until_element_visible(Russian.ruble_symbol)


@pytest.mark.digits_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_digits_russian(driver):
    Russian.getting_to_games(driver)
    for click in range(2):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[4].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.digits_game_instructions_in_russian)
    driver.click(Russian.continue_in_russian)
    driver.click(Russian.begin_in_russian)
    driver.wait_until_element_visible(Russian.digits_game_text)


@pytest.mark.easy_or_hard_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_easy_or_hard_russian(driver):
    Russian.getting_to_games(driver)
    for click in range(3):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[5].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.easy_or_hard_instructions_in_russian)
    driver.wait_until_element_visible(Russian.another_ruble_symbol)
    driver.click(Russian.continue_in_russian)
    driver.click(Russian.begin_in_russian)
    driver.wait_until_element_visible(Russian.easy_or_hard_text)


@pytest.mark.stop_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_stop_russian(driver):
    Russian.getting_to_games(driver)
    for click in range(4):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[6].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.stop_instructions_in_russian)


@pytest.mark.cards_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_cards_russian(driver):
    Russian.getting_to_games(driver)
    for click in range(5):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[7].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.cards_instructions_in_russian)
    driver.click(Russian.continue_in_russian)
    driver.click(Russian.begin_in_russian)
    driver.wait_until_element_visible(Russian.cards_text)
    driver.wait_until_element_visible(Russian.another_ruble_symbol)


@pytest.mark.arrows_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_arrows_russian(driver):
    Russian.getting_to_games(driver)
    for click in range(6):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[8].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.arrows_instructions_in_russian)


@pytest.mark.length_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_length_russian(driver):
    Russian.getting_to_games(driver)
    for click in range(7):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[9].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.length_instructions_in_russian)
    driver.click(Russian.continue_in_russian)
    driver.click(Russian.begin_in_russian)
    driver.wait_until_element_visible(Russian.another_ruble_symbol)


@pytest.mark.towers_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_towers_russian(driver):
    Russian.getting_to_games(driver)
    for click in range(8):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[10].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.towers_instructions_in_russian)
    driver.click(Russian.continue_in_russian)
    driver.click(Russian.begin_in_russian)
    driver.wait_until_element_visible(Russian.towers_text)


@pytest.mark.faces_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_faces_russian(driver):
    Russian.getting_to_games(driver)
    for click in range(9):
        driver.click(GamesPage.scroll_right_btn)
    play = driver.find_elements(By.XPATH, Russian.play_games_buttons['selector'])
    play[11].click()
    driver.switch_frame(GamesPage.iframe)
    driver.wait_until_element_visible(Russian.faces_game_instructions_in_russian)
    driver.click(Russian.continue_in_russian)
    driver.click(Russian.begin_in_russian)
    driver.wait_until_element_visible(Russian.faces_game_text)


@pytest.mark.video_interview_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.flaky(reruns=2)
@pytest.mark.regression_no_csv
def test_video_interview_russian(driver):
    LoginPage.login_spanish_user(driver, '/login')
    driver.wait_until_element_visible(GamesApplicationPage.applications_logo)
    driver.click(GamesApplicationPage.main_complete_video_interview_button)
    driver.wait_until_element_visible(Russian.select_dropdown_interview)
    driver.click(Russian.select_dropdown_interview)
    driver.click(Russian.russian_option_interview)
    driver.click(Russian.select_dropdown_interview)
    driver.click(DigitalInterview.languages_continue)
    driver.wait_until_element_visible(Russian.configuration_popup)
    driver.click(DigitalInterview.languages_continue)
    driver.wait_until_element_visible(Russian.intro_text)
    driver.wait_until_element_visible(Russian.introduction_title_in_russian)
    driver.click(Russian.continue_in_russian_interview)
    driver.wait_until_element_visible(Russian.about_company_in_russian)
    driver.click(Russian.continue_in_russian_interview)
    driver.wait_until_element_visible(Russian.what_to_expect)
    driver.wait_until_element_visible(Russian.min_russian)
    driver.wait_until_element_visible(Russian.emphasis_text)
    driver.click(Russian.continue_in_russian_interview)
    driver.wait_until_element_visible(Russian.setup_text)
    driver.click(Russian.start_tests_interview)
    driver.wait_until_element_visible(Russian.config_text)


@pytest.mark.audio_interview_russian
@pytest.mark.russian
@pytest.mark.translations
@pytest.mark.flaky(reruns=2)
@pytest.mark.regression_no_csv
# another commit
def test_audio_interview_russian(driver):
    LoginPage.login_user_audio_interview(driver, '/login')
    driver.wait_until_element_visible(GamesApplicationPage.applications_logo)
    driver.click(GamesApplicationPage.main_complete_video_interview_button)
    driver.wait_until_element_visible(Russian.select_dropdown_interview)
    driver.click(Russian.select_dropdown_interview)
    driver.click(Russian.russian_option_interview)
    driver.click(Russian.select_dropdown_interview)
    driver.click(DigitalInterview.languages_continue)
    driver.wait_until_element_visible(Russian.configuration_popup)
    driver.click(DigitalInterview.languages_continue)
    driver.wait_until_element_visible(Russian.intro_text)
    driver.wait_until_element_visible(Russian.introduction_title_in_russian)
    driver.click(Russian.continue_in_russian_interview)
    driver.wait_until_element_visible(Russian.about_company_in_russian)
    driver.click(Russian.continue_in_russian_interview)
    driver.wait_until_element_visible(Russian.what_to_expect)
    driver.wait_until_element_visible(Russian.min_russian)
    driver.wait_until_element_visible(Russian.emphasis_text)
    driver.click(Russian.continue_in_russian_interview)
    driver.wait_until_element_visible(Russian.setup_text)
    driver.click(Russian.start_tests_interview)
    driver.wait_until_element_visible(Russian.config_text)
