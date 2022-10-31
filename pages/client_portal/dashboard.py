from tests.ui_tests.pages.base_page import BasePage


class Dashboard(BasePage):
    high_chart = {
        'description': 'Dashboard chart',
        'selector': '.highcharts-container',
    }
    insights_button = {
        'description': 'Insights button',
        'selector': '[title="Workforce Insights"]',
    }
    iframe = {
        'description': 'Mode report',
        'selector': 'iframe',
    }
    main_chart = {
        'description': 'main chart',
        'selector': '#main-chart',
    }
    nested_iframe = {
        'description': 'Nested iframe in the Mode report',
        'selector': '.embed-iframe',
    }
    main_chart_header = {
        'description': 'main chart header',
        'selector': '.chart-header-main',
    }
    main_chart_header_right_arrow = {
        'description': 'main chart header right arrow',
        'selector': '.trait-click-arrow > text:nth-child(3)',
    }
