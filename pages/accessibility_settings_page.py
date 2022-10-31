from tests.ui_tests.pages.base_page import BasePage


class AccessibilitySettingsPage(BasePage):
    no_mods_checkbox = {
        'description': 'Version without modifications checkbox',
        'selector': '#no-mods-checkbox',
    }
    continue_button = {
        'description': 'continue button',
        'selector': '#accessibility-submit',
    }
