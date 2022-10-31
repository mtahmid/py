from tests.ui_tests.pages.base_page import BasePage


class Downloads(BasePage):
    downloads_button = {
        'description': 'Downloads button',
        'selector': '[title="Downloads"]',
    }
    file_name_row_title = {
        'description': 'File Name row title',
        'selector': '//div[contains(text(), "File Name")]',
        'type': 'xpath',
    }
