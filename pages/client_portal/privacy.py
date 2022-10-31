from tests.ui_tests.pages.base_page import BasePage


class Privacy(BasePage):
    privacy_button = {
        'description': 'Privacy button',
        'selector': '[title="Privacy Settings"]',
    }
    delete_account_button = {
        'description': 'Delete Account button',
        'selector': '[ng-click="openDeleteModal()"]',
    }
