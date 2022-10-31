from tests.ui_tests.pages.client_portal.filters import Filters
from tests.ui_tests.pages.base_page import BasePage

from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class Candidates(BasePage):
    candidates_button = {
        'description': 'Candidates button',
        'selector': '[title="Candidates"]',
    }
    status_row_title = {
        'description': 'Status row title',
        'selector': '//p[contains(text(), "Status")]',
        'type': 'xpath',
    }
    export_selected_rows_icon = {
        'description': 'Export selected rows icon',
        'selector': '#Bulk-RR-DL-Popup-Copy',
    }
    candidate_row = {
        'description': 'Each candidate row',
        'selector': '._3QnBlbEIQB0wXPplr5RUQt ',
    }
    bulk_assign_3_candidates = {
        'description': 'Bulk assign 3 candidates icon',
        'selector': '[data-tip="Bulk assign 3 candidates"]',
    }
    evaluators_bulk = {
        'description': 'evaluators under bulk assign',
        'selector': '._2sKXLMj-XzUoi1M-Cuq5W_ [type="checkbox"]',
    }
    assign_bulk = {
        'description': 'Assign button under bulk',
        'selector': '//*[text()="Assign"]',
        'type': 'xpath',
    }
    archive_selected_rows_icon = {
        'description': 'Archive selected rows icon',
        'selector': '#Individual-Candidate-Detail-View---OPTION-2',
    }
    download_selected_rows_icon = {
        'description': 'Download selected rows icon',
        'selector': '#Bulk-Actions---RR-Beta',
    }
    items_per_page_dropdown = {
        'description': 'Items per page dropdown',
        'selector': '.Select-value-label',
    }
    hundred_items_per_page = {
        'description': 'Items per page dropdown',
        'selector': '//span[contains(text(), "100 Items per Page")]',
        'type': 'xpath',
    }
    ten_items_per_page = {
        'description': 'Items per page dropdown',
        'selector': '#react-select-2--option-0',
    }
    fifty_items_per_page = {
        'description': 'Items per page dropdown',
        'selector': '#react-select-2--option-2',
    }
    hundred_items_dropdown = {
        'description': 'Items per page dropdown',
        'selector': '#react-select-2--option-3',
    }
    candidate_search_field = {
        'description': 'Candidate search',
        'selector': '[placeholder="Search for a name or email..."]',
    }
    candidate_search_button = {
        'description': 'Candidate search',
        'selector': '.fa-search',
    }
    apply_filters = {
        'description': 'Apply filters',
        'selector': '//button[contains(text(), "Apply Filters")]',
        'type': 'xpath',
    }
    games_first_position = {
        'description': 'First position listed in the Games tab',
        'selector': '(//div[contains(@id, "text_position")])[1]',
        'type': 'xpath',
    }
    games_second_position = {
        'description': 'Second position listed in the Games tab',
        'selector': '(//div[contains(@id, "text_position")])[2]',
        'type': 'xpath',
    }
    position_descending_arrow = {
        'description': 'Sortable descending arrow for Positions',
        'selector': '(//*[contains(@id, "Sorting-Arrows")])[15]',
        'type': 'xpath',
    }
    position_ascending_arrow = {
        'description': 'Sortable ascending arrow for Positions',
        'selector': '(//*[contains(@id, "Sorting-Arrows")])[14]',
        'type': 'xpath',
    }
    competency_container = {
        'description': '1-5 evaluation container',
        'selector': '.competency-container',
    }
    video_player = {
        'description': 'Response video player',
        'selector': '.videoPlayer',
    }
    download_report = {
        'description': 'Download report button',
        'selector': '.report-container',
    }
    iframe = {
        'description': 'evaluation iframe',
        'selector': 'iframe',
    }
    report_tab = {
        'description': 'evaluation report tab',
        'selector': '(//a[contains(text(), "report")])',
        'type': 'xpath',
    }
    responses_tab = {
        'description': 'evaluation responses tab',
        'selector': '(//a[contains(text(), "response")])',
        'type': 'xpath',
    }
    center_message = {
        'description': 'recruiter page message',
        'selector': '//p[@class="center-message"]',
        'type': 'xpath',
    }
    search_results = {
        'description': 'Search results on "Andy"',
        'selector': "//span[contains(text(), 'Andy')]",
        'type': 'xpath',
    }
    interviews_tab = {
        'description': 'Interviews tab',
        'selector': '//button[contains(text(), "Interviews")]',
        'type': 'xpath',
    }
    candidate_card_games_tab = {
        'description': 'Candidate card games tab',
        'selector': '//h4[contains(text(), "Games")]',
        'type': 'xpath',
    }
    candidate_card_interview_tab = {
        'description': 'Candidate card interview tab',
        'selector': '//h4[contains(text(), "Interviews")]',
        'type': 'xpath',
    }
    candidate_card_applied_to = {
        'description': 'Candidate card position applied to text',
        'selector': '//h3[contains(text(), "Positions Applied To")]',
        'type': 'xpath',
    }
    candidate_card_fit_to = {
        'description': 'Candidate card fit to other position text',
        'selector': '//h3[contains(text(), "Fit To Other Positions")]',
        'type': 'xpath',
    }
    candidate_card_no_interview_text = {
        'description': 'Candidate card no interviews yet text',
        'selector': '//h3[contains(text(), "Candidate has no interviews yet")]',
        'type': 'xpath',
    }
    interviews_tab = {
        'description': 'Interviews tab',
        'selector': '//button[contains(text(), "Interviews")]',
        'type': 'xpath',
    }
    invited = {
        'description': 'Invited dates on the candidates page',
        'selector': '//a[6]/p/span[contains(text(), "/")]',
        'type': 'xpath',
    }
    interview_invited = {
        'description': 'Invited dates on the interviews tab',
        'selector': '//p[contains(text(), "/")]',
        'type': 'xpath',
    }
    unarchive_button = {
        'description': 'Unarchive button on candidates page',
        'selector': '[data-tip*="Unarchive"]',
    }
    unavailable_checkbox = {
        'description': 'Unavailable checkbox on a scored candidate',
        'selector': '._2C-2nMYm2rwcBSctskYAZP [disabled]',
    }
    number_of_pages = {
        'description': 'Number of pages on the candidates tab',
        'selector': '//div[@class="ED0r5MJMk9fV-R0X5FmXM "]',
        'type': 'xpath',
    }
    empty = {
        'description': 'Text for position status',
        'selector': "//h3[contains(text(), 'Sorry')]",
        'type': 'xpath',
    }
    completed = {
        'description': 'Completed dates on the candidates page',
        'selector': '//a[7]/p/span[contains(text(), "/")]',
        'type': 'xpath',
    }
    interviews_status = {
        'description': 'Candidates status on the candidates page',
        'selector': '[data-for*="Status"] > span',
    }
    interview_position_text = {
        'description': 'Text for position status',
        'selector': '//a[2]/div/div/span[text()]',
        'type': 'xpath'
    }
    evaluate_interview = {
        'description': 'Evaluate interview button under Candidate card',
        'selector': '//span[contains(text(),"Evaluate Interview")]',
        'type': 'xpath'
    }
    evaluation_submitted = {
        'description': 'Evaluate interview button under Candidate card',
        'selector': '//span[contains(text(),"Evaluation Submitted")]',
        'type': 'xpath'
    }
    exit_button = {
        'description': 'Exit button under Candidate card',
        'selector': 'a[href="/c/p/candidates/"]',
    }
    pymetrics_evaluator = {
        'description': 'Evaluators list',
        'selector': "//div[text() = 'Py Metrics']",
        'type': 'xpath'
    }
    pymetrics_evaluators = {
        'description': 'Pymetrics as an evaluator under interview',
        'selector': "//*[text() = 'Py Metrics']",
        'type': 'xpath'
    }
    scored_popup = {
        'description': 'Pop up regarding candidates being already scored',
        'selector': '//i[@class="fa fa-exclamation-triangle"]',
        'type': 'xpath'
    }
    three_evaluators = {
        'description': 'Shows 3 evaluators for a candidate',
        'selector': '//span[contains(text(), "4 evaluators")]',
        'type': 'xpath'
    }
    assign_evaluators = {
        'description': 'Assign evaluators button',
        'selector': '//button[contains(text(), "Assign")]',
        'type': 'xpath'
    }
    evaluation = {
        'description': 'Evaluation status in the Candidate card',
        'selector': "//div[@class='lbh2pOkR8M-9Ig2waXshU ']",
        'type': 'xpath'
    }
    not_started_evaluation = {
        'description': 'Not Started evaluation under candidates card',
        'selector': '//div[(text() = "Not Started")]',
        'type': 'xpath'
    }
    in_progress_evaluation = {
        'description': 'In progress evaluation under candidates card',
        'selector': '//div[(text() = "In Progress")]',
        'type': 'xpath'
    }
    submitted_evaluation = {
        'description': 'Submitted evaluation under candidates card',
        'selector': '//div[(text() = "Submitted")]',
        'type': 'xpath'
    }
    evaluators = {
        'description': 'Evaluators list',
        'selector': '._2MR6CWi8CRGt3mCLYpUQsz ',
    }
    cancel_removing = {
        'description': 'Cancel removing button',
        'selector': '//*[text()="Cancel"]',
        'type': 'xpath'
    }
    evaluators_column = {
        'description': 'Evaluators list',
        'selector': "//p[text() = 'Evaluator(s)']",
        'type': 'xpath'
    }
    score_column = {
        'description': 'Score column name',
        'selector': "//p[text() = 'Score']",
        'type': 'xpath'
    }
    next_page_arrow = {
        'description': 'An arrow for the next page to appear',
        'selector': '//i[@class="fa fa-angle-right"]',
        'type': 'xpath',
    }
    previous_page_arrow = {
        'description': 'An arrow for the next page to appear',
        'selector': '//i[@class="fa fa-angle-left"]',
        'type': 'xpath',
    }
    apply_assigned_evaluator = {
        'description': 'Apply button under Candidate card',
        'selector': '#apply-assigned-evaluator',
    }
    archive_1_row = {
        'description': 'An archive button just for 1 candidate',
        'selector': '//div[@data-tip="Archive 1 selected rows"]',
        'type': 'xpath'
    }
    archive_3_rows = {
        'description': 'An archive button just for 3 candidates',
        'selector': '//div[@data-tip="Archive 3 selected rows"]',
        'type': 'xpath'
    }
    status_column = {
        'description': 'A header name for status column',
        'selector': '//p[text() = "Status"]',
        'type': 'xpath'
    }
    archive_25_rows = {
        'description': 'An archive button just for 25 candidates',
        'selector': '//div[@data-tip="Archive 25 selected rows"]',
        'type': 'xpath'
    }
    export_1_row = {
        'description': 'An Export button just for 1 candidate',
        'selector': '//div[@data-tip="Export 1 selected rows"]',
        'type': 'xpath'
    }
    export_3_rows = {
        'description': 'An Export button just for 3 candidates',
        'selector': '//div[@data-tip="Export 3 selected rows"]',
        'type': 'xpath'
    }
    export_25_rows = {
        'description': 'An Export button just for 25 candidates',
        'selector': '//div[@data-tip="Export 25 selected rows"]',
        'type': 'xpath'
    }
    download_csv_template_link = {
        'description': 'Download CSV invite template link',
        'selector': '//*[contains(text(),"download the CSV template")]',
        'type': 'xpath'
    }
    batman_user = {
        'description': 'A user with the last name Batman',
        'selector': '//span[contains(text(), "Batman")]',
        'type': 'xpath'
    }
    ratings = {
        'description': 'Ratings from 1 to 5',
        'selector': '//div[@class="rating"]/div',
        'type': 'xpath'
    }
    evaluators_checkboxes = {
        'description': 'Evaluators checkboxes under candidates card',
        'selector': '._256eRZpFyC3MH-2dbgIv2h input',
    }
    evaluators_names = {
        'description': 'Evaluators names under candidates card',
        'selector': '.G7VcK6nFh2gj1HbjqFdz- ',
    }
    evaluators_dropdown = {
        'description': 'Evaluators list inside the candidate modal',
        'selector': '#modify-evaluators-button',
    }
    search_bar = {
        'description': 'Search for an evaluator',
        'selector': '//input[@placeholder]',
        'type': 'xpath'
    }
    alex_evaluator = {
        'description': 'Alex Lapkouski evaluator',
        'selector': '//div[contains(text(), "Alex.Lapkouski")]',
        'type': 'xpath'
    }
    testorg_logo = {
        'description': 'TestOrg logo image in CP',
        'selector': '[alt="TestOrg"]',
    }
    recruiter_report_download_button = {
        'description': 'Recruiter report download button',
        'selector': '._2LFmuFP-Q2cOPG0z2Kz-NQ',
    }

    def disable_invited_30_days(driver):
        driver.click(Filters.filters_dropdown)
        driver.wait_until_element_visible(Filters.recommendation_text)
        driver.click(Filters.invited_30d)
        driver.click(Filters.apply_filters_button)
        driver.wait_until_element_visible(Candidates.completed, delay=120)

    def disable_invited_30_days_interview(driver):
        driver.click(Candidates.interviews_tab)
        driver.wait_until_element_visible(Candidates.interviews_status, delay=30)
        time.sleep(5)
        driver.click(Filters.filters_dropdown)
        driver.wait_until_element_visible(Filters.invited_30d)
        driver.click(Filters.invited_30d)

    def checkbox(self, index):
        checkbox = {
            'description': 'checkbox {}'.format(index),
            'selector': '(//input[@type="checkbox"])[{}]'.format(index),
            'type': 'xpath',
        }
        return checkbox

# flake8: noqa
