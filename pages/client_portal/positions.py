from tests.ui_tests.pages.base_page import BasePage


class Positions(BasePage):
    positions_button = {
        'description': 'Positions button',
        'selector': '[title="Positions"]',
    }
    position_card_progress_bar_title = {
        'description': 'Position card progress bar title',
        'selector': '//h3[contains(text(), "Position Progress")]',
        'type': 'xpath',
    }
    position_card_candidate_pipeline_chart = {
        'description': 'Position card progress bar title',
        'selector': '.highcharts-background',
    }
    position_more_filters = {
        'description': 'More Filters button',
        'selector': '[data-for="otherFiltersDisabled"]',
    }
    positions_filters_checkboxes = {
        'description': 'Filters options',
        'selector': '[type=checkbox]',
    }
    position_apply_filters = {
        'description': 'Apply filters button under positions tab',
        'selector': "//button[contains(text(),'Apply')]",
        'type': 'xpath',
    }
    single_status = {
        'description': 'Each status under each position',
        'selector': '//div[@style="font-size: 0.75rem;"]',
        'type': 'xpath',
    }
    collecting_data_status = {
        'description': 'Stage status under Positions tab',
        'selector': '//p[text()="Collecting Data"]',
        'type': 'xpath',
    }
    positions_filters = {
        'description': 'Filter by positions under Positions tab',
        'selector': "//i[@class='fa fa-briefcase']",
        'type': 'xpath',
    }
    clear_filters = {
        'description': 'Clear Filters results',
        'selector': "//*[text()='Clear Filters']",
        'type': 'xpath',
    }
    assessment = {
        'description': 'Assessment section under Positions card',
        'selector': "//h4[contains(text(), 'Assessment')]",
        'type': 'xpath',
    }
    candidate_link = {
        'description': 'Candidate link under Positions card',
        'selector': "//td[contains(text(), 'Candidate Link')]",
        'type': 'xpath',
    }
    positions_statuses = {
        'description': 'Positions statuses',
        'selector': '._1Mu11XQ3i_LCbVKyxqDYv3._1wzKMWc_9mqQSM_eR4mGm4 ',
    }
    search_field = {
        'description': 'Positions search field',
        'selector': '[placeholder]',
    }
    positions = {
        'description': 'Number of positions',
        'selector': '._1Mu11XQ3i_LCbVKyxqDYv3 ',
    }
