from tests.ui_tests.pages.base_page import BasePage


class RecruiterReport(BasePage):
    report_body = {
        'description': 'Downloadable report body',
        'selector': '.downloadable-report-body',
    }
    header = {
        'description': 'Header',
        'selector': 'div.header',
    }
    header_content = {
        'description': 'Header Content',
        'selector': '.header-content',
    }
    score = {
        'description': 'Score',
        'selector': '.score',
    }
    model_factors = {
        'description': 'Model factors',
        'selector': '.model-factors',
    }
