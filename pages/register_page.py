from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.privacy_page import PrivacyPage

# todo: Find more accurate descriptions


class RegisterPage(BasePage):
    email = {
        'description': 'registration email textbox',
        'selector': 'input[name="email"]',
    }
    password = {
        'description': 'registration password textbox',
        'selector': 'input[name="password"]',
    }
    confirm_password = {
        'description': 'confirm password',
        'selector': 'input[name="confirm_password"]',
    }
    register_button = {
        'description': 'register button',
        'selector': '#register-submit'
    }
    logo = {
        'description': 'logo',
        'selector': '.self-end.logo'
    }
    language_dropdown = {
        'description': 'language dropdown menu',
        'selector': '#language',
    }
    english_language_option = {
        'description': 'english option in the language dropdown',
        'selector': '[label="English"]',
    }
    spanish_language_option = {
        'description': 'Spanish option in the language dropdown',
        'selector': '[label="Español"]',
    }
    russian_language_option = {
        'description': 'Russian option in the language dropdown',
        'selector': '[label="Русский"]',
    }

    def get_email_value(self):
        attribute_value = self.driver.return_attribute(self.email, 'value')
        self.driver.take_screenshot()
        return attribute_value

    def set_password(self, password):
        self.driver.type_keys(self.password, password)

    def set_confirm_password(self, password):
        self.driver.type_keys(self.confirm_password, password)

    def click_register_button(self):
        self.driver.take_screenshot()
        self.driver.click(self.register_button)
        return PrivacyPage(self.driver)

    def wait_until_page_load(self):
        self.driver.wait_until_element_visible(self.logo)
        self.driver.add_metadata_cookie()
        return self
