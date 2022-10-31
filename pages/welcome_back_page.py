from tests.ui_tests.pages.base_page import BasePage


# todo: Find this page and supply more accurate descriptions.

class WelcomeBackPage(BasePage):
    title = {
        'description': 'page title',
        'selector': 'h2.dark-blue',
    }
    replay_button = {
        'description': 'replay button',
        'selector': '.jade-background',
    }
    resubmit_button = {
        'description': 'resubmit button',
        'selector': '#interrupts-app .watermelon-background',
    }

    def get_title(self):
        self.driver.wait_until_element_visible(self.title)
        self.driver.take_screenshot()
        return self.driver.return_text(self.title)

    def click_replay(self):
        self.driver.wait_until_element_visible(self.replay_button)
        self.driver.take_screenshot()
        self.driver.click(self.replay_button)

    def click_resubmit(self):
        self.driver.wait_until_element_visible(self.replay_button)
        self.driver.take_screenshot()
        self.driver.click(self.resubmit_button)
