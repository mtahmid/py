from tests.ui_tests.pages.base_page import BasePage


class WidgetPage(BasePage):
    login_button = {
        'description': 'Widget login button',
        'selector': 'button.blue-chill-background',
    }
    widget_auth_page = {
        'description': 'Widget auth page content selector',
        'selector': '.widget-auth-page',
    }
