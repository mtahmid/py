from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage


class GamesConfigPage(BasePage):
    submit_button = {
        'description': 'games config page submit button',
        'selector': '#accessibility-submit',
    }
    language_dropdown = {
        'description': 'Native Language dropdown menu',
        'selector': '#language',
    }
    language_dropdown_nederlands = {
        'description': 'Language dropdown Nederlands',
        'selector': '//*[contains(text(), "Nederlands")]',
        'type': 'xpath'
    }
    dyslexia_checkbox = {
        'description': 'Version modified for Dyslexia checkbox',
        'selector': '[ng-model="accessibility.dyslexic"]',
    }

    def click_submit(self):
        self.driver.take_screenshot()
        self.driver.click(self.submit_button)
        return GamesApplicationPage(self.driver)
