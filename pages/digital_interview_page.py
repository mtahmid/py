from tests.ui_tests.pages.base_page import BasePage


class DigitalInterview(BasePage):
    languages_continue = {
        'description': 'Continue button under languages pop up',
        'selector': '#language-selection-button',
    }
    main_continue = {
        'description': 'Continue button on the welcome page',
        'selector': '.page-wrap.welcome-page > button',
    }
    company_continue = {
        'description': 'Continue button on the company page',
        'selector': '.btn-pink',
    }
    what_to_expect_continue = {
        'description': 'Continue button on the what to expect page',
        'selector': '#what-to-expect',
    }
    start_tests = {
        'description': 'Start tests button',
        'selector': '#start-automated-testing-button',
    }
    tests_info = {
        'description': 'Info about the tests',
        'selector': '.test-heading',
    }
