from tests.ui_tests.pages.base_page import BasePage


class WorkforceInsights(BasePage):
    fluidity_button = {
        'description': 'Fluidity button',
        'selector': '//*[contains(text(), "Fluidity")]',
        'type': 'xpath'
    }
    fluidity_copy = {
        'description': 'Workforce Insights fluidity copy',
        'selector': '//*[contains(text(), "answer")]',
        'type': 'xpath'
    }
    header = {
        'description': 'Insights header',
        'selector': '//*[contains(text(), "pymetrics Insights")]',
        'type': 'xpath'
    }
    employees_button = {
        'description': 'Traits button',
        'selector': '//*[contains(text(), "Employees")]',
        'type': 'xpath'
    }
    employees_copy = {
        'description': 'Workforce Insights traits copy',
        'selector': '//*[contains(text(), "internal")]',
        'type': 'xpath'
    }
    im_chart = {
        'description': 'IM Chart',
        'selector': '#im-chart',
    }
    iframe = {
        'description': 'Mode iframe',
        'selector': 'iframe',
    }
    clusters_graph = {
        'description': 'Clusters summary',
        'selector': '.Cluster',
    }
    clusters = {
        'description': 'All clusters',
        'selector': '.node',
    }
    insights_graph = {
        'description': 'All clusters',
        'selector': '#im-graph-container',
    }
    attributes_checkboxes = {
        'description': 'Attributes',
        'selector': '#attributes  .checkbox-container',
    }
    filter_toggles = {
        'description': 'Filter toggles',
        'selector': '.Filters .filter .filter_toggle',
    }
    filters_checkboxes = {
        'description': 'Filter checkboxes',
        'selector': '//div[@class="filter_option_checkbox"]/div',
        'type': 'xpath'
    }
    sort_by_dropdown = {
        'description': 'Sort by dropdown',
        'selector': '//span[contains(text(), "Name")]',
        'type': 'xpath'
    }
    cluster_by_dropdown = {
        'description': 'Sort by dropdown',
        'selector': '//span[contains(text(), "Role")]',
        'type': 'xpath'
    }
    cluster_by_position_title = {
        'description': 'Sort by Count',
        'selector': '//div[contains(text(), "Current position title")]',
        'type': 'xpath'
    }
    cluster_by_manager = {
        'description': 'Sort by Count',
        'selector': '//div[text() = "Manager"]',
        'type': 'xpath'
    }
    sort_by_count = {
        'description': 'Sort by Count',
        'selector': '//div[contains(text(), "Count")]',
        'type': 'xpath'
    }
    factor_circles = {
        'description': 'Circles inside the clusters',
        'selector': '.factor-circles circle',
    }
    grid = {
        'description': 'Sort by Grid',
        'selector': '//div[contains(text(), "Grid")]',
        'type': 'xpath'
    }
    positions = {
        'description': 'Positions to filter by',
        'selector': '.im-filter__values li',
    }
    vs = {
        'description': 'One positions vs another',
        'selector': '.vs',
    }
    capabilities_dropdown = {
        'description': 'Capabilities dropdown',
        'selector': '.Dropdown.page-view .toggle',
    }
    capabilities_option = {
        'description': 'Capabilities option',
        'selector': '//div[contains(text(), "Capabilities")]',
        'type': 'xpath'
    }
    different_capabilties = {
        'description': '6 Capabilities',
        'selector': '#capability-title',
    }
    graph_positions = {
        'description': 'Positions under graph',
        'selector': '.tick',
    }
