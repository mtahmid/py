from tests.ui_tests.pages.base_page import BasePage


class CreateAccountPage(BasePage):
    first_name = {
        'description': 'First name input',
        'selector': '#first_name',
    }
    last_name = {
        'description': 'Last name input',
        'selector': '#last_name',
    }
    email = {
        'description': 'email input',
        'selector': '#email',
    }
    password = {
        'description': 'email input',
        'selector': '#password',
    }
    confirm_password = {
        'description': 'email input',
        'selector': '#confirm_password',
    }
    language_dropdown = {
        'description': 'language dropdown',
        'selector': '#language',
    }
    language_dropdown_english = {
        'description': 'Language dropdown English',
        'selector': '//*[contains(text(), "English")]',
        'type': 'xpath'
    }
    submit_button = {
        'description': 'submit button',
        'selector': '#register-submit',
    }
