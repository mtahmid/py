from tests.ui_tests.pages.base_page import BasePage


class Incumbent(BasePage):
    label_text = {
        'description': 'Label text',
        'selector': '//p[contains(text(), "Label")]',
        'type': 'xpath',
    }
    search_icon = {
        'description': 'Incumbent search',
        'selector': '.fa-search',
    }
    incumbents_button = {
        'description': 'Incumbents button',
        'selector': '#Incumbents-Icon---Inactive',
    }
    incumbent_search = {
        'description': 'Incumbent search field',
        'selector': '[placeholder="Search for a name, email or label…"]',
    }
    fedtestinc_user = {
        'description': 'The incumbent for testing search function',
        'selector': '//span[contains(text(), "fedtestinc")]',
        'type': 'xpath'
    }
    incumbents_checkbox = {
        'description': 'Incumbents checkbox',
        'selector': '[type="checkbox"]',
    }
    default_label = {
        'description': 'Default Label',
        'selector': '//span[contains(text(), "Data Collection")]',
        'type': 'xpath',
    }
    fifty_items_per_page = {
        'description': 'Items per page dropdown',
        'selector': '//div[contains(text(), "50 Items per Page")]',
        'type': 'xpath',
    }
    twenty_five_items_per_page = {
        'description': 'Items per page dropdown',
        'selector': '//span[contains(text(), "25 Items per Page")]',
        'type': 'xpath',
    }
    career_growth_tab = {
        'description': 'Career growth tab',
        'selector': '//h4[contains(text(), "Career")]',
        'type': 'xpath',
    }
    no_positions_text = {
        'description': 'No positions text',
        'selector': '//h3[contains(text(), "No recommended positions")]',
        'type': 'xpath',
    }
    incumbents = {
        'description': 'Different incumbents under the page',
        'selector': '._2V1NFA6KOErkK3wCptYMQ3._3PyRYyBZF_qgMyBpb-IzIN.WDLEm2cT4YJmvnplLhVTc',
    }
    whitelist_button = {
        'description': 'Whitelist button',
        'selector': '[data-for="whitelistIncumbentButton"]',
    }
    position_dropdown = {
        'description': 'Position dropdown',
        'selector': '.Select.positionSelect',
    }
    active_position = {
        'description': 'Active position',
        'selector': '//div[contains(@role,"option") and .//text()="Test ACT Position (USA, SC)"]', # noqa
        'type': 'xpath',
    }
    email_textbox = {
        'description': 'Invite email textbox',
        'selector': '[placeholder="Type emails here"]',
    }
    submit_button = {
        'description': 'Submit button',
        'selector': '//button[contains(text(), "Submit")]',
        'type': 'xpath',
    }
    invite_link = {
        'description': 'Invite link',
        'selector': '[rel="noopener noreferrer"]',
    }
    filters_dropdown = {
        'description': 'Filters dropdown',
        'selector': '//button[@class="_2m5PGlvBvB7_jjz-QsZlML "]',
        'type': 'xpath'
    }
    filters_status_checkboxes = {
        'description': 'Filters status checkboxes',
        'selector': '._329H4KeRLS6h_-eKQz5lPN:first-child > div [type]',
    }
    status_checkboxes_text = {
        'description': 'Text for status filter checkboxes',
        'selector': '._329H4KeRLS6h_-eKQz5lPN:first-child > div [data-for]',
    }
    filters_position_check = {
        'description': 'Filters status checkboxes',
        'selector': '._329H4KeRLS6h_-eKQz5lPN:nth-child(2) > div [type]',
    }
    position_check_text = {
        'description': 'Text for status filter checkboxes',
        'selector': '._329H4KeRLS6h_-eKQz5lPN:nth-child(2) > div [data-for]',
    }
