from tests.ui_tests.pages.base_page import BasePage

# todo: Find this page and supply more accurate descriptions.
# todo: Implement delay functionality


class BeforeWeBeginPage(BasePage):
    title = {
        'description': 'page title',
        'selector': '.welcome-title span',
    }
    continue_button = {
        'description': 'continue button',
        'selector': '#welcome-continue-btn',
    }
    welcome_content = {
        'description': 'welcome content text block',
        'selector': '.welcome-content',
    }

    def get_title(self):
        self.driver.take_screenshot()
        return self.driver.return_text(self.title)

    def click_continue(self):
        self.driver.take_screenshot()
        self.driver.click(self.continue_button)
