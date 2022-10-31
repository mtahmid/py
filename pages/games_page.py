from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.traits_report_page import TraitsReportPage
from selenium.webdriver.common.by import By
import time


class GamesPage(BasePage):
    # todo: Get find Elements checked_game_cards working and Delete this.
    checked_game_cards_b = (By.CSS_SELECTOR, '.fa.fa-check-circle')

    checked_game_cards = {
        'description': 'Completed game green check mark icon',
        'selector': '.step-section.desert-storm-background i',
    }
    cards = {
        'description': 'individual game cards',
        'selector': '.card',
    }
    completed_games_header_text = {
        'description': 'x out of 12 complete header text',
        'selector': '#applications .navy-blue-background > h3',
    }
    games_info_popup_close = {
        'description': '"X" button in the "Welcome!" games page popup',
        'selector': '.remodal-wrapper.remodal-is-opened button',
    }
    close_icon = {
        'description': '"X" button for the games',
        'selector': '[class*="exit-icon"]',
    }
    title = {
        'description': 'games page title',
        'selector': '#applications .games-step h2',
    }
    traits_report_title = {
        'description': '"Traits" tab on top of page',
        'selector': '#header-nav-traits',
    }
    games_info_popup_message = {
        'description': 'The entire message in the games info popup modal',
        'selector': '.remodal-wrapper.remodal-is-opened .left-align .left-align.bigger',  # noqa
    }
    games_info_popup_title = {
        'description': 'The title in the games info popup ("Some advice from the experts")',  # noqa
        'selector': '.remodal-wrapper.remodal-is-opened .left-align .regular-font.center-align',  # noqa
    }
    banner_text = {
        'description': 'Page banner text',
        'selector': '.page-wrap h1.regular-font'
    }
    faces_play_button = {
        'description': 'Faces play button',
        'selector': '//application-game-card[1]/a',
        'type': 'xpath',
    }
    iframe = {
        'description': 'Game iframe window',
        'selector': 'iframe',
    }
    blue_continue_button = {
        'description': 'Blue continue button',
        'selector': '.game__button_blue'
    }
    green_start_button = {
        'description': 'Green start button',
        'selector': '.game__button_green'
    }
    return_to_application_button = {
        'description': 'Return to Application button',
        'selector': '//*[contains(text(), "Return to Application")]',
        'type': 'xpath',
    }
    game_player_iframe = {
        'description': 'JS Game player iframe',
        'selector': '#js-game-player',
    }
    scroll_right_btn = {
        'description': 'Scroll right button',
        'selector': '[ng-click="scrollRight();"]',
    }
    replay_games = {
        'description': 'Replay Games button',
        'selector': '[name="selectToReplayGames"]',
    }

    def get_title(self):
        self.driver.wait_until_element_visible(self.title)
        self.driver.take_screenshot()
        return self.driver.return_text(self.title)

    def close_modal(self):
        self.driver.wait_until_element_visible(self.games_info_popup_close)
        self.driver.take_screenshot()
        self.driver.click(self.games_info_popup_close)

    def get_game_cards(self):
        elements = self.driver.return_elements(self.cards)
        return elements

    def get_checked_game_cards(self):
        elements = self.driver.find_elements(*self.checked_game_cards_b)
        # todo: Get this working
        # elements = self.driver.return_elements(self.checked_game_cards)
        return elements

    def navigate_to_traits_report_page(self):
        self.driver.wait_until_element_visible(self.traits_report_title)
        self.driver.take_screenshot()
        self.driver.click(self.traits_report_title)
        return TraitsReportPage(self.driver)

    def get_welcome_model_title(self):
        self.driver.wait_until_element_visible(self.games_info_popup_title)
        self.driver.take_screenshot()
        return self.driver.return_text(self.games_info_popup_title)

    def get_welcome_model_message(self):
        self.driver.waitUntilElementVisible(self.games_info_popup_message)
        self.driver.take_screenshot()
        return self.driver.return_text(self.games_info_popup_message)

    def contains_complete_the_games_message(self, message):
        message_contain = 'Please complete the required games and we ' \
            + 'will submit your results supporting your application to'
        return message_contain in message

    def contains_result_submitted_message(self, message):
        message_contain = 'We have submitted your existing results ' \
            + 'supporting your application to'
        return message_contain in message

    def click_games_play_button(self, index):
        playbutton = {
            'description': f'Game {index} Play button',
            'selector': f'//application-game-card[{index}]/a',
            'type': 'xpath',
        }
        return self.driver.click(playbutton)

# flake8: noqa
