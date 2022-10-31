from tests.ui_tests.pages.base_page import BasePage


# todo: Find this page and supply more accurate descriptions.


class TraitsReportPage(BasePage):
    category_dropdown = {
        'description': 'Category dropdown',
        'selector': '.type-select-title.ng-binding',
    }
    trait_cards = {
        'description': 'Trait cards',
        'selector': 'trait-card.card',
    }
    title = {
        'description': 'page title',
        'selector': '#page-content .page-banner .page-wrap h1',
    }
    data_warning_message = {
        'description': 'data warning message',
        'selector': '#page-content incomplete-games .regular-font',
    }
    complete_button = {
        'description': 'Complete button',
        'selector': '.watermelon-background',
    }
    explainer_card = {
        'description': 'Overview of pymetrics approach',
        'selector': '.explainer-card',
    }
    breakdown_nav = {
        'description': 'Breakdown nav',
        'selector': '#results-breakdown-nav',
    }

    def get_title(self):
        self.driver.wait_until_element_visible(self.title)
        self.driver.take_screenshot()
        return self.driver.return_text(self.title)

    def get_data_warning_message(self):
        self.driver.wait_until_element_visible(self.data_warning_message)
        self.driver.take_screenshot()
        return self.driver.return_text(self.data_warning_message)
