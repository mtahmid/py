import pytest
import os
import csv
import random

from selenium.webdriver.common.action_chains import ActionChains
from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.privacy_page import PrivacyPage
from tests.ui_tests.pages.create_account_page import CreateAccountPage
from tests.ui_tests.pages.client_portal.candidates import Candidates
from tests.ui_tests.pages.accessibility_settings_page import (
    AccessibilitySettingsPage,
)
from tests.ui_tests.pages.before_we_begin_page import BeforeWeBeginPage
from tests.ui_tests.pages.games_application_page import GamesApplicationPage
from tests.ui_tests.pages.client_portal.candidates_invite_single import (
    CandidateInviteSingle,
)
from tests.ui_tests.pages.client_portal.incumbents import Incumbent
from tests.ui_tests.pages.client_portal.dashboard import Dashboard
from tests.ui_tests.pages.client_portal.filters import Filters

from selenium.webdriver.common.by import By
import tests.ui_tests.utils.configs as configs
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys


@pytest.mark.candidates
@pytest.mark.client_portal
def test_candidates_button(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + "/c/p/candidates")
    status = driver.return_text(Candidates.status_row_title)
    assert status == "Status"


@pytest.mark.candidates
@pytest.mark.client_portal
def test_bulk_icon_display(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + "/c/p/candidates")
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("1"))
    driver.click(candidate.checkbox("2"))
    driver.wait_until_element_visible(Candidates.export_selected_rows_icon)
    driver.wait_until_element_visible(Candidates.archive_selected_rows_icon)
    driver.wait_until_element_visible(Candidates.download_selected_rows_icon)


@pytest.mark.candidates
@pytest.mark.client_portal
def test_export_selected_rows_icon(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + "/c/p/candidates")
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("1"))
    driver.click(candidate.checkbox("2"))
    driver.click(Candidates.export_selected_rows_icon)


@pytest.mark.candidates
@pytest.mark.client_portal
def test_archive_icon(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + "/c/p/candidates")
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("1"))
    driver.click(Candidates.archive_selected_rows_icon)


@pytest.mark.candidates
@pytest.mark.client_portal
def test_download_selected_rows_icon(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + "/c/p/candidates")
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("1"))
    driver.click(Candidates.download_selected_rows_icon)


@pytest.mark.regression_no_csv
@pytest.mark.search_by_name
@pytest.mark.flaky(reruns=2)
def test_search_button(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.wait_until_element_visible(Candidates.completed, delay=120)
    Candidates.disable_invited_30_days(driver)
    driver.type_keys(Candidates.candidate_search_field, "andy")
    search_field = driver.find_element(
        By.CSS_SELECTOR, Candidates.candidate_search_field["selector"]
    )
    search_field.send_keys(Keys.RETURN)
    results = driver.return_elements(Candidates.search_results)
    assert len(results) > 5


@pytest.mark.regression_no_csv
@pytest.mark.search_button_email
@pytest.mark.flaky(reruns=2)
def test_search_button_email(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.wait_until_element_visible(Candidates.completed, delay=120)
    Candidates.disable_invited_30_days(driver)
    driver.type_keys(
        Candidates.candidate_search_field, "andy.kim@pymetrics.com"
    )
    search_field = driver.find_element(
        By.CSS_SELECTOR, Candidates.candidate_search_field["selector"]
    )
    search_field.send_keys(Keys.RETURN)
    results = driver.return_elements(Candidates.search_results)
    assert len(results) <= 1


@pytest.mark.interview_search_button_email
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_search_button_email(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    Candidates.disable_invited_30_days_interview(driver)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Candidates.interviews_status)
    driver.type_keys(
        Candidates.candidate_search_field, "andy.kim@pymetrics.com"
    )
    search_field = driver.find_element(
        By.CSS_SELECTOR, Candidates.candidate_search_field["selector"]
    )
    search_field.send_keys(Keys.RETURN)
    results = driver.return_elements(Candidates.search_results)
    assert len(results) <= 1


@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.positions_games_sort
@pytest.mark.flaky(reruns=2)
def test_positions_games_sort(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(
        Candidates.position_descending_arrow, delay=120
    )
    driver.click(Candidates.position_descending_arrow)
    time.sleep(2)
    position_1 = driver.return_text(Candidates.games_first_position)
    position_2 = driver.return_text(Candidates.games_second_position)
    assert position_1 == position_2
    driver.click(Candidates.position_ascending_arrow)
    time.sleep(2)
    position_1 = driver.return_text(Candidates.games_first_position)
    position_2 = driver.return_text(Candidates.games_second_position)
    assert position_1 == position_2


@pytest.mark.candidate_card_games
@pytest.mark.candidates
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_candidate_card_games(driver):
    LoginPage.login_recruiter(
        driver, "/c/p/candidates/assessments/199907/games"
    )
    driver.wait_until_element_visible(
        Candidates.candidate_card_games_tab, delay=120
    )
    driver.wait_until_element_visible(Candidates.candidate_card_applied_to)
    driver.wait_until_element_visible(Candidates.candidate_card_fit_to)
    driver.click(Candidates.candidate_card_interview_tab)
    driver.wait_until_element_visible(
        Candidates.candidate_card_no_interview_text
    )


@pytest.mark.candidate_card_interview
@pytest.mark.candidates
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_candidate_card_interviews(driver):
    LoginPage.login_recruiter(
        driver, "/c/p/candidates/assessments/199907/games"
    )
    driver.wait_until_element_visible(
        Candidates.candidate_card_interview_tab, delay=120
    )
    driver.click(Candidates.candidate_card_interview_tab)
    driver.wait_until_element_visible(
        Candidates.candidate_card_no_interview_text, delay=120
    )


@pytest.mark.C914108
@pytest.mark.evaluation
@pytest.mark.candidates
@pytest.mark.client_portal
def test_assigned_evaluator(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Candidates.candidates_button)
    driver.navigate_to(
        configs.url + "/video/evaluation/9/1193973/?current_view=response"
    )
    driver.wait_until_element_visible(Candidates.competency_container)


@pytest.mark.C914107
@pytest.mark.evaluation
@pytest.mark.candidates
@pytest.mark.client_portal
def test_unassigned_evaluator(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Candidates.candidates_button)
    driver.navigate_to(
        configs.url + "/video/evaluation/9/1197226/?current_view=response"
    )
    with pytest.raises(Exception) as excinfo:
        element = driver.find_element_by_css_selector(
            Candidates.competency_container["selector"]
        )
    unable = "Unable to locate element"
    exception = str(excinfo)
    assert exception.find(unable)


@pytest.mark.C1247059
@pytest.mark.evaluation
@pytest.mark.candidates
@pytest.mark.client_portal
def test_assigned_audio_evaluator(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Candidates.candidates_button)
    driver.navigate_to(configs.url + "/video/evaluation/45/1192906/response")
    driver.wait_until_element_visible(Candidates.competency_container)


@pytest.mark.C1247058
@pytest.mark.evaluation
@pytest.mark.candidates
@pytest.mark.client_portal
def test_unassigned_audio_evaluator(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Candidates.candidates_button)
    driver.navigate_to(configs.url + "/video/evaluation/45/1196453/response")
    with pytest.raises(Exception) as excinfo:
        element = driver.find_element_by_css_selector(
            Candidates.competency_container["selector"]
        )
    unable = "Unable to locate element"
    exception = str(excinfo)
    assert exception.find(unable)


@pytest.mark.interviews_tab
@pytest.mark.client_portal
def test_interviews_tab(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + "/c/p/candidates")
    driver.wait_until_element_visible(Candidates.interviews_tab)
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.evaluators_column)
    driver.wait_until_element_visible(Candidates.score_column)
    driver.wait_until_element_visible(Candidates.interviews_status)


@pytest.mark.single_select
@pytest.mark.client_portal
@pytest.mark.row_selection
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_single_select(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.wait_until_element_visible(Candidates.invited, delay=120)
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("5"))
    driver.click(Candidates.next_page_arrow)
    driver.wait_until_element_visible(Candidates.invited)
    time.sleep(2)
    driver.click(Candidates.previous_page_arrow)
    driver.wait_until_element_visible(Candidates.archive_1_row)


@pytest.mark.multiple_select
@pytest.mark.client_portal
@pytest.mark.row_selection
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_multiple_select(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.wait_until_element_visible(Candidates.invited, delay=120)
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("5"))
    driver.click(candidate.checkbox("6"))
    driver.click(candidate.checkbox("7"))
    driver.click(Candidates.next_page_arrow)
    driver.wait_until_element_visible(Candidates.invited, delay=60)
    driver.click(Candidates.previous_page_arrow)
    driver.wait_until_element_visible(Candidates.archive_3_rows)


@pytest.mark.select_with_filter
@pytest.mark.client_portal
@pytest.mark.row_selection
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_select_with_filter(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.wait_until_element_visible(Candidates.invited, delay=120)
    time.sleep(3)
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("5"))
    time.sleep(3)
    driver.click(Filters.filters_dropdown)
    driver.click(Filters.status_completed)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Candidates.status_column)


@pytest.mark.select_all_on_page
@pytest.mark.client_portal
@pytest.mark.row_selection
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_select_all_on_page(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.wait_until_element_visible(Candidates.invited, delay=120)
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("1"))
    driver.click(Candidates.next_page_arrow)
    driver.wait_until_element_visible(Candidates.invited)
    driver.click(Candidates.previous_page_arrow)
    driver.wait_until_element_visible(Candidates.archive_25_rows)


@pytest.mark.single_select_video
@pytest.mark.client_portal
@pytest.mark.row_selection
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_single_select_video(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status, delay=120)
    time.sleep(6)
    # Interviews page needs more time to load properly
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("5"))
    driver.click(Candidates.next_page_arrow)
    driver.wait_until_element_visible(Candidates.interviews_status)
    driver.click(Candidates.previous_page_arrow)
    driver.wait_until_element_visible(Candidates.export_1_row)


@pytest.mark.multiple_select_video
@pytest.mark.client_portal
@pytest.mark.row_selection
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_multiple_select_video(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status, delay=60)
    time.sleep(6)
    # Interviews page needs more time to load properly
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("5"))
    driver.click(candidate.checkbox("6"))
    driver.click(candidate.checkbox("7"))
    driver.click(Candidates.next_page_arrow)
    driver.wait_until_element_visible(Candidates.interviews_status)
    time.sleep(3)
    # Interviews page needs more time to load properly
    driver.click(Candidates.previous_page_arrow)
    time.sleep(3)
    # Interviews page needs more time to load properly
    driver.wait_until_element_visible(Candidates.export_3_rows)


@pytest.mark.select_with_filter_video
@pytest.mark.client_portal
@pytest.mark.row_selection
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_select_with_filter_video(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status, delay=60)
    time.sleep(6)
    # Interviews page needs more time to load properly
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("5"))
    driver.click(Filters.filters_dropdown)
    driver.click(Filters.registered_interview)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Candidates.score_column)


@pytest.mark.select_all_video
@pytest.mark.client_portal
@pytest.mark.row_selection
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_select_all_video(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status, delay=120)
    time.sleep(6)
    # Interviews page needs more time to load properly
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("1"))
    driver.click(Candidates.next_page_arrow)
    driver.wait_until_element_visible(Candidates.interviews_status)
    time.sleep(3)
    # Interviews page needs more time to load properly
    driver.click(Candidates.previous_page_arrow)
    time.sleep(3)
    # Interviews page needs more time to load properly
    driver.wait_until_element_visible(Candidates.export_25_rows)


@pytest.mark.C910805
@pytest.mark.csv
def test_invite_csv_template_download(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + "/c/p/candidates/invite/upload")
    driver.click(Candidates.download_csv_template_link)
    time.sleep(1)  # Needed for the download to complete
    assert os.path.exists(os.getcwd() + "/downloads/candidate-template.csv")
    with open("downloads/candidate-template.csv", "r") as f:
        reader = csv.reader(f)
        row = next(reader)
        assert row[0] == "Email Address"
        assert row[1] == "First Name"
        assert row[2] == "Last Name"


@pytest.mark.items_per_page_games
@pytest.mark.client_portal
@pytest.mark.row_displayed
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=3)
def test_items_per_page_games(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.wait_until_element_visible(Candidates.completed, delay=120)
    driver.click(Candidates.items_per_page_dropdown)
    driver.click(Candidates.ten_items_per_page)
    driver.wait_until_element_visible(Filters.status)
    number_of_candidates = driver.find_elements(
        By.XPATH, Filters.status["selector"]
    )
    assert len(number_of_candidates) <= 10
    driver.click(Candidates.items_per_page_dropdown)
    driver.click(Candidates.fifty_items_per_page)
    driver.wait_until_element_visible(Filters.status)
    number_of_candidates = driver.find_elements(
        By.XPATH, Filters.status["selector"]
    )
    assert 25 < len(number_of_candidates) <= 50
    driver.click(Candidates.items_per_page_dropdown)
    driver.click(Candidates.hundred_items_dropdown)
    driver.wait_until_element_visible(Filters.status)
    number_of_candidates = driver.find_elements(
        By.XPATH, Filters.status["selector"]
    )
    assert 50 < len(number_of_candidates) <= 100


@pytest.mark.items_per_page_games_filter
@pytest.mark.client_portal
@pytest.mark.row_displayed
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_items_per_page_games_filter(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.wait_until_element_visible(Candidates.completed, delay=120)
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("3"))
    driver.click(Candidates.items_per_page_dropdown)
    driver.click(Candidates.ten_items_per_page)
    driver.wait_until_element_visible(Candidates.status_row_title)


@pytest.mark.items_per_page_video
@pytest.mark.client_portal
@pytest.mark.row_displayed
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_items_per_page_video(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status, delay=120)
    time.sleep(6)
    # Interviews page needs more time to load properly
    driver.click(Candidates.items_per_page_dropdown)
    time.sleep(1)
    driver.click(Candidates.ten_items_per_page)
    driver.wait_until_element_visible(Candidates.interviews_status)
    time.sleep(5)
    # Interviews page needs more time to load properly
    number_of_candidates = driver.find_elements(
        By.CSS_SELECTOR, Candidates.interviews_status["selector"]
    )
    assert len(number_of_candidates) <= 10
    driver.click(Candidates.items_per_page_dropdown)
    driver.click(Candidates.fifty_items_per_page)
    driver.wait_until_element_visible(Candidates.interviews_status)
    time.sleep(5)
    # Interviews page needs more time to load properly
    number_of_candidates = driver.find_elements(
        By.CSS_SELECTOR, Candidates.interviews_status["selector"]
    )
    assert 25 < len(number_of_candidates) <= 50
    driver.click(Candidates.items_per_page_dropdown)
    driver.click(Candidates.hundred_items_dropdown)
    driver.wait_until_element_visible(Candidates.interviews_status)
    time.sleep(5)
    # Interviews page needs more time to load properly
    number_of_candidates = driver.find_elements(
        By.CSS_SELECTOR, Candidates.interviews_status["selector"]
    )
    assert 50 < len(number_of_candidates) <= 100


@pytest.mark.items_per_page_video_filter
@pytest.mark.client_portal
@pytest.mark.row_displayed
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_items_per_page_video_filter(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.wait_until_element_visible(Candidates.completed, delay=120)
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status, delay=120)
    time.sleep(6)
    # Interviews page needs more time to load properly
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("3"))
    driver.click(Candidates.items_per_page_dropdown)
    driver.click(Candidates.ten_items_per_page)
    driver.wait_until_element_visible(Candidates.status_row_title)


@pytest.mark.single_candidate_invite
@pytest.mark.client_portal
@pytest.mark.C910809
def test_single_candidate_invite_email_form(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + "/c/p/candidates/invite/single")
    driver.click(CandidateInviteSingle.position_dropdown)
    driver.click(CandidateInviteSingle.active_position)
    driver.type_keys(CandidateInviteSingle.first_name_textbox, "test")
    driver.type_keys(CandidateInviteSingle.last_name_textbox, "test")
    driver.type_keys(CandidateInviteSingle.email_name_textbox, "test@test.com")
    driver.click(CandidateInviteSingle.submit)
    email = driver.return_text(CandidateInviteSingle.bcc_email)
    assert email == "test@test.com"
    driver.wait_until_element_visible(
        CandidateInviteSingle.send_from_placeholder_name
    )
    driver.wait_until_element_visible(
        CandidateInviteSingle.reply_to_placeholder
    )
    subject_value = driver.return_attribute(
        CandidateInviteSingle.email_subject, "value"
    )
    assert subject_value == "test"
    driver.return_elements(CandidateInviteSingle.variables_available)


@pytest.mark.interview_name_search
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_name_search(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    Candidates.disable_invited_30_days_interview(driver)
    driver.type_keys(Candidates.candidate_search_field, "batman")
    search_field = driver.find_element(
        By.CSS_SELECTOR, Candidates.candidate_search_field["selector"]
    )
    search_field.send_keys(Keys.RETURN)
    driver.wait_until_element_visible(Candidates.batman_user, delay=120)


@pytest.mark.bulk_valid
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_bulk_valid(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    Candidates.disable_invited_30_days_interview(driver)
    driver.click(Filters.registered_interview)
    driver.click(Filters.test_act_position)
    driver.click(Filters.unassigned_evaluator)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(
        Candidates.interview_position_text, delay=120
    )
    time.sleep(5)
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("5"))
    driver.click(candidate.checkbox("6"))
    driver.click(candidate.checkbox("7"))
    driver.click(Candidates.bulk_assign_3_candidates)
    time.sleep(4)
    evaluators = driver.find_elements(
        By.CSS_SELECTOR, Candidates.evaluators_bulk["selector"]
    )
    evaluators[11].click()
    assign = driver.find_elements(By.XPATH, Candidates.assign_bulk["selector"])
    assign[25].click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.accept()
    driver.wait_until_element_visible(Candidates.interview_position_text)


@pytest.mark.bulk_scored
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_bulk_scored(driver):
    LoginPage.login_recruiter(driver, "/c/p/candidates")
    Candidates.disable_invited_30_days_interview(driver)
    driver.click(Filters.scored)
    driver.click(Filters.test_act_position)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Candidates.interview_position_text)
    time.sleep(4)
    candidate = Candidates(driver)
    driver.click(candidate.checkbox("5"))
    driver.click(candidate.checkbox("6"))
    driver.click(candidate.checkbox("7"))
    driver.click(Candidates.bulk_assign_3_candidates)
    driver.wait_until_element_visible(Candidates.scored_popup)


@pytest.mark.client_portal
@pytest.mark.candidate_whitelist
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_candidate_whitelist(driver):
    random_num = random.randint(1, 9 ** 11)
    email = "test_automation+test" + str(random_num) + "@example.com"

    LoginPage.login_recruiter(driver, "/c/p/candidates")
    driver.wait_until_element_visible(Candidates.testorg_logo, delay=120)
    driver.wait_until_element_visible(Candidates.completed)
    driver.click(CandidateInviteSingle.whitelist)
    driver.click(Incumbent.position_dropdown)
    driver.wait_until_element_visible(Incumbent.active_position, delay=60)
    driver.click(Incumbent.active_position)
    driver.type_keys(Incumbent.email_textbox, email)
    driver.click(Incumbent.submit_button)
    link = driver.return_text(Incumbent.invite_link)
    driver.click(CandidateInviteSingle.exit)
    action = ActionChains(driver)
    logout = driver.find_element(
        By.CSS_SELECTOR, CandidateInviteSingle.logout["selector"]
    )
    action.move_to_element(logout).perform()
    time.sleep(3)
    driver.click(CandidateInviteSingle.logout)
    driver.wait_until_element_visible(CandidateInviteSingle.login_form)
    driver.navigate_to(link)
    driver.type_keys(
        CreateAccountPage.first_name,
        "testthirtycharacterstestthirtycharacters",
    )  # noqa
    driver.type_keys(
        CreateAccountPage.last_name, "testthirtycharacterstestthirtycharacters"
    )  # noqa
    driver.type_keys(CreateAccountPage.email, email)
    driver.type_keys(CreateAccountPage.password, "t3st!ngg")
    driver.type_keys(CreateAccountPage.confirm_password, "t3st!ngg")
    driver.click(CreateAccountPage.language_dropdown)
    driver.click(CreateAccountPage.language_dropdown_english)
    driver.click(CreateAccountPage.submit_button)
    privacy_page = PrivacyPage(driver)
    time.sleep(5)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()
    driver.click(PrivacyPage.testorg_notice)
    driver.click(PrivacyPage.submit_consent_button)
    driver.wait_until_element_visible(BeforeWeBeginPage.continue_button)
    driver.click(BeforeWeBeginPage.continue_button)
    driver.click(AccessibilitySettingsPage.no_mods_checkbox)
    driver.click(AccessibilitySettingsPage.continue_button)
    driver.wait_until_element_visible(GamesApplicationPage.complete_games)
    invited = driver.find_elements(
        By.XPATH, GamesApplicationPage.invite_date["selector"]
    )
    get_date = invited[0]
    date_parsed = datetime.strptime(get_date.text, "%B %d, %Y").date()
    assert date_parsed == datetime.today().date()
