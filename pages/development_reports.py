from tests.ui_tests.pages.base_page import BasePage


class DevelopmentReports(BasePage):
    dev_report_download = {
        'description': 'Development reports download button',
        'selector': '#development-report-download-btn',
    }
    development_report_header = {
        'description': 'Development reports header',
        'selector': '//div[contains(text(), "Development Report")]',
        'type': 'xpath'
    }
    header_logo = {
        'description': 'Header logo',
        'selector': '#header-logo',
    }
    development_report_headers = {
        'description': 'Development reports date',
        'selector': '.header-container .header-text',
    }
    development_report_name = {
        'description': 'Development reports name',
        'selector': '//div[contains(text(), "Alex Test")]',
        'type': 'xpath'
    }
    about_this_report = {
        'description': 'About this report section',
        'selector': '.intro-section.about-section',
    }
    overview = {
        'description': 'Overview of the report',
        'selector': '.intro-section.overview-section',
    }
    interpreting = {
        'description': 'Interpreting the report',
        'selector': '.intro-section.interpret-section',
    }
    summary_title = {
        'description': 'Summary title',
        'selector': '.summary-title',
    }
    summary_text = {
        'description': 'Summary text',
        'selector': '.summary-text',
    }
    legend = {
        'description': 'Legend on the page',
        'selector': '.legend',
    }
    factors_section = {
        'description': 'Factors section',
        'selector': '.summary-factor-section ',
    }
    summary_factor = {
        'description': 'Different factors',
        'selector': '.summary-factor',
    }
    quartile = {
        'description': 'Selected quartile',
        'selector': '.quartile.selected',
    }
    factor_title = {
        'description': 'Factor title',
        'selector': '.factor-title',
    }
    factor_details = {
        'description': 'Factor Details',
        'selector': '.factor-details-content',
    }
    date = {
        'description': 'Factor Details',
        'selector': '.factor-details-content',
    }
    leadership_report = {
        'description': 'Leadership report text',
        'selector': '//div[contains(text(), "leadership")]',
        'type': 'xpath'
    }
