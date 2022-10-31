from tests.ui_tests.pages.base_page import BasePage
# todo: Go to this url and make more accurate descriptions.
# todo: Implement delay functionality


class GamesApplicationPage(BasePage):
    complete_games_button = {
        'description': 'button for complete games',
        'selector': 'div.application-next-step button',
    }
    application_complete_games_button = {
        'description': 'Complete Games button in Application',
        'selector': '(//a[contains(text(), "Complete Games")])[2]',
        'type': 'xpath',
    }
    no_game_replay_complete_games_button = {
        'description': 'Complete Games button in no game replay application',
        'selector': '(//a[contains(text(), "Complete Games")])[3]',
        'type': 'xpath',
    }
    card_complete_games_button = {
        'description': 'button for complete games on application card',
        'selector': '//button[contains(text(), "Complete Games")]',
        'type': 'xpath',
    }
    action_items_complete_games_button = {
        'description': 'Complete Games button under Action Items',
        'selector': '//a[contains(text(), "Complete Games")]',
        'type': 'xpath',
    }
    completion_title = {
        'description': 'completion title',
        'selector': '#applications .game-modal h3.center-align.hug',
    }
    modal = {
        'description': 'modal on games application page',
        'selector': '.remodal-wrapper.remodal-is-opened button.remodal-close',
    }
    next_step_complete_games_button = {
        'description': 'Complete Games button under Application Steps',
        'selector': '.application-next-step.center-align button',
    }
    resubmit_button = {
        'description': 'Keep My Gameplay button',
        'selector': '.layout.horizontal.center-center .watermelon-background',
    }
    replay_games = {
        'description': 'Keep My Gameplay button',
        'selector': '[ng-click="replayGames($event, true);"]',
    }
    unchecked_games_circle = {
        'description': 'Unchecked gray games circle',
        'selector': '#applications .step-section.light-shadow-background i',
    }
    checked_games_circle = {
        'description': 'checked green games circle',
        'selector': '#applications .step-section.desert-storm-background i',
    }
    thank_you_completion_text = {
        'description': 'Thank you for completing pymetrics!',
        'selector': '#applications .step-section > p',
    }
    view_traits_button = {
        'description': 'View Results button',
        'selector': '(//a[contains(text(), "View Results")])[1]',
        'type': 'xpath',
    }
    complete_video_interview_button = {
        'description': 'Complete Digital Interview button',
        'selector': '(//a[contains(text(), "Complete Digital Interview")])[2]',
        'type': 'xpath',
    }
    main_complete_video_interview_button = {
        'description': 'Complete Digital Interview button on applications',
        'selector': '(//a[contains(text(), "Complete Digital Interview")])',
        'type': 'xpath',
    }
    invite_date = {
        'description': 'The date of invitation',
        'selector': '//span[contains(text(), ",")]',
        'type': 'xpath',
    }
    help_tab = {
        'description': 'Help tab',
        'selector': '#header-nav-help',
    }
    complete_games = {
        'description': 'Complete games under Application pop up',
        'selector': '#next-step-button-games-advice',
    }
    help_header = {
        'description': 'Help header',
        'selector': '//h1[contains(text(), "Help")]',
        'type': 'xpath',
    }
    dashboard_text = {
        'description': 'Dashboard text',
        'selector': '//h1[contains(text(), "dashboard")]',
        'type': 'xpath',
    }
    home_tab = {
        'description': 'Home tab',
        'selector': '#header-nav-applications',
    }
    dropdown_logout = {
        'description': 'Logout button in account dropdown',
        'selector': '[href="/logout/"]',
    }
    finish_and_play_games_btn = {
        'description': 'Finish & Play Games button',
        'selector': '//button[contains(text(), "Finish & Play Games")]',
        'type': 'xpath',
    }
    language_dropdown = {
        'description': 'Language Dropdown',
        'selector': '#language',
    }
    english_option = {
        'description': 'English language option',
        'selector': '//option[contains(text(), "English")]',
        'type': 'xpath',
    }
    games_advice_img = {
        'description': 'Games Advice Image',
        'selector': '[alt="games advice image"]',
    }
    i_understand_btn = {
        'description': 'I Understand button on Continue to the Games modal',
        'selector': 'button.watermelon-background.fattie.ng-binding',
    }
    view_results = {
        'description': 'View Results button under application pop up',
        'selector': '#view-trait-results-button',
    }
    back_to_application = {
        'description': 'Back to application button',
        'selector': "a [class*='fa fa-chevron-left']",
    }
    games_close_icon = {
        'description': 'Games close icon',
        'selector': "[class*='exit-icon']",
    }
    games_info = {
        'description': 'Games info popup',
        'selector': '[data-remodal-id="games-info"]',
    }
    applications_logo = {
        'description': 'Applications logo',
        'selector': '#logo',
    }
    interview_complete_page = {
        'description': 'Digital interview complete page',
        'selector': '.complete-page',
    }
    interview_feedback_page = {
        'description': 'Digital interview feedback page',
        'selector': '.feedback-page',
    }

    def click_complete_games(self):
        self.driver.take_screenshot()
        self.driver.click(self.complete_games_button)

    def click_next_step_complete_games(self):
        self.driver.take_screenshot()
        self.driver.click(self.next_step_complete_games_button)

    def close_modal(self):
        self.driver.take_screenshot()
        self.driver.click(self.modal)

    def click_resubmit_button(self):
        self.driver.wait_until_element_visible(self.resubmit_button)
        self.driver.take_screenshot()
        self.driver.click(self.resubmit_button)

    def get_completion_title(self):
        self.driver.wait_until_element_visible(self.completion_title)
        self.driver.take_screenshot()
        return self.driver.return_text(self.completion_title)

    def are_all_games_completed(self, message):
        split_words = message.split()
        return split_words[0] == split_words[3]

    def unchecked_games_circle_visible(self):
        self.driver.take_screenshot()
        return self.driver.wait_until_element_visible(
            self.unchecked_games_circle)

    def checked_games_circle_visible(self):
        self.driver.take_screenshot()
        return self.driver.wait_until_element_visible(
            self.checked_games_circle)

    def get_thank_you_completion_text(self):
        self.driver.wait_until_element_visible(self.thank_you_completion_text)
        self.driver.take_screenshot()
        return self.driver.return_text(self.thank_you_completion_text)

    def get_to_the_games(self):
        self.driver.click(
            GamesApplicationPage.application_complete_games_button)
        self.driver.click(GamesApplicationPage.language_dropdown)
        self.driver.click(GamesApplicationPage.english_option)
        self.driver.click(GamesApplicationPage.finish_and_play_games_btn)

    def bypass_game_advice(self):
        """
        click through games advice and game confirm modal
        """
        self.driver.click(
            GamesApplicationPage.action_items_complete_games_button)
        self.driver.wait_until_element_visible(
            GamesApplicationPage.games_advice_img)
        self.driver.click(GamesApplicationPage.language_dropdown)
        self.driver.click(GamesApplicationPage.english_option)
        self.driver.wait_until_element_visible(
            GamesApplicationPage.finish_and_play_games_btn)
        self.driver.click(GamesApplicationPage.finish_and_play_games_btn)
        self.driver.wait_until_element_visible(
            GamesApplicationPage.i_understand_btn
        )
        self.driver.click(GamesApplicationPage.i_understand_btn)
        self.driver.wait_until_element_visible(
            GamesApplicationPage.games_close_icon
        )
        self.driver.click(GamesApplicationPage.games_close_icon)

    def lets_get_to_the_games(self):
        """
        clicks through 'let's get to the games' screen
        """
        self.driver.click(
            GamesApplicationPage.application_complete_games_button)
        self.driver.click(GamesApplicationPage.language_dropdown)
        self.driver.click(GamesApplicationPage.english_option)
        self.driver.click(GamesApplicationPage.finish_and_play_games_btn)
