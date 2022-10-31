from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Filters(BasePage):
    filters_dropdown = {
        'description': 'Filters dropdown',
        'selector': '//button[@data-for="otherFiltersDisabled"]',
        'type': 'xpath'
    }
    filters_status_checkboxes = {
        'description': 'Filters status checkboxes',
        'selector': '._2dWgaQKyo0IbW6qgWYL79d:first-child > div [type]',
    }
    status_checkboxes_text = {
        'description': 'Text for status filter check boxes',
        'selector': '._2dWgaQKyo0IbW6qgWYL79d:first-child > div [data-for]',
    }
    apply_filters_button = {
        'description': 'Apply filters button',
        'selector': '//button[contains(text(), "Apply Filters")]',
        'type': 'xpath'
    }
    clear_filters = {
        'description': 'Clear all filters button',
        'selector': '#prospective_candidates-clear-filters-button',
    }
    status = {
        'description': 'The text of the status',
        'selector': '//a//p[text()]',
        'type': 'xpath'
    }
    filters_recommendation_check = {
        'description': 'Filters recommendation checkboxes',
        'selector': '._2dWgaQKyo0IbW6qgWYL79d:nth-child(2) > div [type]',
    }
    recommendation_check_text = {
        'description': 'Text for recommendation filter checkboxes',
        'selector': '._2dWgaQKyo0IbW6qgWYL79d:nth-child(2) > div [data-for]',
    }
    recommendation_text = {
        'description': 'Text for recommendation status',
        'selector': '//a[5]/div/div/span[text()]',
        'type': 'xpath'
    }
    filters_position_check = {
        'description': 'Filters position checkboxes',
        'selector': '._2dWgaQKyo0IbW6qgWYL79d:nth-child(3) > div [type]',
    }
    position_check_text = {
        'description': 'Text for position filter checkboxes',
        'selector': '._2dWgaQKyo0IbW6qgWYL79d:nth-child(3) > div [data-for]',
    }
    position_text = {
        'description': 'Text for position status',
        'selector': '//a[4]/div/div/span[text()]',
        'type': 'xpath'
    }
    search = {
        'description': 'Search field',
        'selector': '//input[@placeholder="Search for others"]',
        'type': 'xpath'
    }
    alex = {
        'description': 'Invited by Alex',
        'selector': '[data-for="Alex.Lapkouski@pymetrics.com"]',
    }
    emails = {
        'description': 'Emails needed',
        'selector': '//a[3]/div/div/span[contains(text(), "@")]',
        'type': 'xpath'
    }
    flagged_check = {
        'description': 'Flagged checkbox under filters',
        'selector': "//span[text()='Flagged']",
        'type': 'xpath'
    }
    full_flag = {
        'description': 'Flag which is filled with black color',
        'selector': 'g[fill="#333333"]',
    }
    archived_check = {
        'description': 'Archived checkbox under filters',
        'selector': "//span[text()='Archived']",
        'type': 'xpath'
    }
    invited_24h = {
        'description': 'The checkbox for Invited in the past 24 hours option',
        'selector': '//span[text()="Past 24 Hours"]',
        'type': 'xpath'
    }
    invited_7d = {
        'description': 'The checkbox for Invited in the past 7 days option',
        'selector': '//span[text()="Past 7 Days"]',
        'type': 'xpath'
    }
    invited_30d = {
        'description': 'The checkbox for Invited in the past 30 days option',
        'selector': '//span[text()="Past 30 Days"]',
        'type': 'xpath'
    }
    invited_12m = {
        'description': 'The checkbox for Invited in the past 12  months',
        'selector': '//span[text()="Past 12 Months"]',
        'type': 'xpath'
    }
    invited_custom = {
        'description': 'The checkbox for custom dates',
        'selector': '//span[text()="Custom"]',
        'type': 'xpath'
    }
    dates_input_field = {
        'description': 'The fields for dates input',
        'selector': '.react-datepicker__input-container input',
    }
    completed_24h = {
        'description': 'The checkbox for Completed in the past 24 hours',
        'selector': '(//span[text()="Past 24 Hours"])[2]',
        'type': 'xpath'
    }
    completed_7d = {
        'description': 'The checkbox for Completed in the past 7 days',
        'selector': '(//span[text()="Past 7 Days"])[2]',
        'type': 'xpath'
    }
    completed_30d = {
        'description': 'The checkbox for Completed in the past 30 days',
        'selector': '(//span[text()="Past 30 Days"])[2]',
        'type': 'xpath'
    }
    completed_12m = {
        'description': 'The checkbox for Completed in the past 12 months',
        'selector': '(//span[text()="Past 12 Months"])[2]',
        'type': 'xpath'
    }
    completed_custom = {
        'description': 'The checkbox for custom dates',
        'selector': '(//span[text()="Custom"])[2]',
        'type': 'xpath'
    }
    interview_position = {
        'description': 'Different positions at Interviews tab',
        'selector': '._2dWgaQKyo0IbW6qgWYL79d:nth-child(4) > div [data-for]',
    }
    interview_position_check = {
        'description': 'Checkboxes of different positions at Interviews',
        'selector': '._2dWgaQKyo0IbW6qgWYL79d:nth-child(4) > div [type]',
    }
    pymetrics_evaluator = {
        'description': 'Checkboxes to choose Py Metrics as an evaluator',
        'selector': '[data-for*="Py Metrics"]',
    }
    fedor_garin = {
        'description': 'Checkboxes to choose Fedor as an evaluator',
        'selector': '[data-for*="Fedor Garin"]',
    }
    unassigned_evaluator = {
        'description': 'Checkboxes to choose Unassigned evaluator',
        'selector': '[data-for*="Unassigned"]',
    }
    evaluators_input = {
        'description': 'Evaluators search field',
        'selector': '[placeholder="Search evaluators"]',
    }
    test_act_position = {
        'description': 'Test act position under filters',
        'selector': '[data-for="Test ACT Position (USA, SC)"]',
    }
    scored = {
        'description': 'Scored candidates under filter',
        'selector': '//span[text()="Scored"]',
        'type': 'xpath'
    }
    evaluation_status_check = {
        'description': 'Checkboxes for evaluation statuses',
        'selector': '._2dWgaQKyo0IbW6qgWYL79d:nth-child(2) > div [type]',
    }
    evaluators_list = {
        'description': 'List of evaluators under Filter',
        'selector': '._3bh6BDKR0JLW8ZiBh56qaz:nth-child(3) div [data-for]',
    }
    evaluation_status = {
        'description': 'Evaluation statuses',
        'selector': '._2dWgaQKyo0IbW6qgWYL79d:nth-child(2) > div [data-for]',
    }
    status_completed = {
        'description': 'Checkbox with Completed status',
        'selector': '//span[text() = "Completed"]',
        'type': 'xpath'
    }
    registered_interview = {
        'description': 'Checkbox with Registered status',
        'selector': '//span[text()="Registered"]',
        'type': 'xpath'
    }

    def disable_invited_30d(driver):
        LoginPage.login_recruiter(driver, '/c/p/candidates')
        driver.wait_until_element_visible(Filters.status, delay=120)
        driver.click(Filters.filters_dropdown)
        driver.wait_until_element_visible(Filters.recommendation_text)
        driver.click(Filters.invited_30d)

    def input_valid_date(driver):
        driver.click(Filters.invited_custom)
        dates_input = driver.find_elements(By.CSS_SELECTOR,
                                           Filters.dates_input_field['selector'])
        dates_input[0].send_keys(Keys.BACKSPACE * 10)
        dates_input[0].send_keys("05/01/2020")
        dates_input[1].click()
        dates_input[1].clear()
        dates_input[1].send_keys(Keys.BACKSPACE * 10)
        dates_input[1].send_keys("05/02/2020")
        dates_input[1].send_keys(Keys.RETURN)
        driver.click(Filters.apply_filters_button)

    def input_same_date(driver):
        driver.click(Filters.invited_custom)
        dates_input = driver.find_elements(By.CSS_SELECTOR,
                                           Filters.dates_input_field['selector'])
        dates_input[0].send_keys(Keys.BACKSPACE * 10)
        dates_input[0].send_keys("05/01/2020")
        dates_input[1].click()
        dates_input[1].clear()
        dates_input[1].send_keys(Keys.BACKSPACE * 10)
        dates_input[1].send_keys("05/01/2020")
        dates_input[1].send_keys(Keys.RETURN)
        driver.click(Filters.apply_filters_button)

    def input_wrong_date(driver):
        driver.click(Filters.invited_custom)
        dates_input = driver.find_elements(By.CSS_SELECTOR,
                                           Filters.dates_input_field['selector'])
        dates_input[0].send_keys(Keys.BACKSPACE * 10)
        dates_input[0].send_keys("08/01/2020")
        dates_input[1].click()
        dates_input[1].clear()
        dates_input[1].send_keys(Keys.BACKSPACE * 10)
        dates_input[1].send_keys("05/01/2020")
        dates_input[1].send_keys(Keys.RETURN)
        driver.click(Filters.apply_filters_button)
