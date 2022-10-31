from tests.ui_tests.pages.base_page import BasePage

# todo: Find this page and supply more accurate descriptions.


class PrivacyPage(BasePage):
    title = {
        'description': 'page title',
        'selector': '#privacy-header h2',
    }
    modal = {
        'description': 'privacy page modal',
        'selector': '.remodal-wrapper.remodal-is-opened button.blue-chill-background',  # noqa
    }
    consent_all_checkbox = {
        'description': 'consent all checkbox',
        'selector': '#consent-all',
    }
    submit_consent_button = {
        'description': 'submit consent button',
        'selector': '#submit-consent'
    }
    next_button = {
        'description': 'next button',
        'selector': 'button.blue-chill-background'
    }
    data_controllers_tab = {
        'description': 'Data Controllers Tab',
        'selector': '#controllersLink',
    }
    controller_description_1 = {
        'description': 'First sentence of the privacy notice controllers \
            description',
        'selector': '//*[contains(text(), "Pymetrics, Inc.")]',
        'type': 'xpath',
    }
    controller_pymetrics_inc = {
        'description': 'Pymetrics, Inc controller header',
        'selector': '.header.ng-binding',
    }
    testorg_notice = {
        'description': 'Checkbox for Pymetrics org',
        'selector': '#notice-1',
    }

    def get_title(self):
        self.driver.wait_until_element_visible(self.title)
        self.driver.take_screenshot()
        return self.driver.return_text(self.title)

    def close_modal(self):
        self.driver.wait_until_element_visible(self.modal)
        self.driver.take_screenshot()
        self.driver.click(self.modal)

    def click_consent_all(self):
        self.driver.click(self.consent_all_checkbox)

    def click_next_button(self):
        self.driver.click(self.next_button)

    def submit_consent(self):
        self.driver.click(self.submit_consent_button)
