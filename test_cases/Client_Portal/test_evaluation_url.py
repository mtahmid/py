import pytest
import time

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.client_portal.filters import Filters
from tests.ui_tests.pages.client_portal.candidates import Candidates
from selenium.webdriver.common.by import By

import tests.ui_tests.utils.configs as configs
from selenium.webdriver.common.keys import Keys


@pytest.mark.cp_admin
@pytest.mark.client_portal
@pytest.mark.evaluation_url
def test_no_response_cp(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Candidates.candidates_button)
    url = (
        "/c/p/candidates/assessments/497275/video/1179583/11/"
        "?current_view=response"
    )
    driver.navigate_to(configs.url + url)
    time.sleep(3)  # waiting for client portal to load
    driver.switch_frame(Candidates.iframe)
    driver.wait_until_element_visible(Candidates.report_tab)
    with pytest.raises(Exception) as excinfo:
        element = driver.find_element_by_css_selector(
            Candidates.video_player["selector"]
        )
    unable = "Unable to locate element"
    exception = str(excinfo)
    assert exception.find(unable)


@pytest.mark.cp_admin
@pytest.mark.client_portal
@pytest.mark.evaluation_url
def test_response_report_ats(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Candidates.candidates_button)
    # same interview as above, but ats link
    url = "/video/evaluation/11/1179583/response"
    driver.navigate_to(configs.url + url)
    driver.wait_until_element_visible(Candidates.video_player)
    driver.click(Candidates.report_tab)
    driver.wait_until_element_visible(Candidates.download_report)


@pytest.mark.cp_admin
@pytest.mark.client_portal
@pytest.mark.evaluation_url
def test_no_report_cp(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Candidates.candidates_button)
    url = (
        "/c/p/candidates/assessments/519085/video/1206998/9/"
        "?current_view=response"
    )
    driver.navigate_to(configs.url + url)
    time.sleep(3)  # waiting for client portal to load
    driver.switch_frame(Candidates.iframe)
    driver.wait_until_element_visible(Candidates.video_player)
    with pytest.raises(Exception) as excinfo:
        element = driver.find_element_by_xpath(
            Candidates.report_tab["selector"]
        )
    unable = "Unable to locate element"
    exception = str(excinfo)
    assert exception.find(unable)


@pytest.mark.cp_admin
@pytest.mark.client_portal
@pytest.mark.evaluation_url
@pytest.mark.regression
def test_nothing_ats(driver):
    LoginPage.login_recruiter(driver, "/c/p")
    driver.wait_until_element_visible(Candidates.candidates_button)
    # same interview as above, but ats link
    url = "/video/evaluation/9/1206998/?current_view=response"
    driver.navigate_to(configs.url + url)
    message = driver.return_text(Candidates.center_message)
    assert message == "Currently there is no content to view"


@pytest.mark.evaluation_one_to_five
@pytest.mark.client_portal
@pytest.mark.evaluation_url
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_evaluation_one_to_five(driver):
    LoginPage.login_recruiter(
        driver,
        "/c/p/candidates/assessments/495562/video/1178191/9"
        "/?current_view=response",
    )
    driver.wait_until_element_visible(Candidates.iframe, delay=120)
    driver.switch_frame(Candidates.iframe)
    time.sleep(5)
    driver.wait_until_element_visible(Candidates.ratings, delay=120)
    ratings = driver.return_elements(Candidates.ratings)
    assert len(ratings) == 5


@pytest.mark.candidate_card_update
@pytest.mark.client_portal
@pytest.mark.evaluation_url
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_candidate_card_update(driver):
    LoginPage.login_recruiter(
        driver, "/c/p/candidates/assessments/557226/video/1238494/"
    )
    driver.wait_until_element_visible(
        Candidates.evaluators_checkboxes, delay=120
    )
    evaluators = driver.return_elements(Candidates.evaluators_checkboxes)
    index = 0
    while index < 3:
        evaluators[index].click()
        index += 1
    driver.click(Candidates.apply_assigned_evaluator)
    driver.click(Candidates.exit_button)
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status)
    driver.click(Filters.filters_dropdown)
    driver.click(Filters.invited_30d)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Candidates.status_column, delay=120)
    time.sleep(5)
    # Interviews page needs more time to load properly
    driver.type_keys(Candidates.candidate_search_field, "Automation user")
    search_field = driver.find_element(
        By.CSS_SELECTOR, Candidates.candidate_search_field["selector"]
    )
    search_field.send_keys(Keys.RETURN)
    driver.wait_until_element_visible(Candidates.three_evaluators, delay=120)
    driver.click(Candidates.three_evaluators)
    evaluators = driver.return_elements(Candidates.evaluators_checkboxes)
    index = 0
    while index < 3:
        evaluators[index].click()
        index += 1
    driver.click(Candidates.apply_assigned_evaluator)
    driver.wait_until_element_visible(
        Candidates.apply_assigned_evaluator, delay=120
    )


@pytest.mark.evaluators_dropdown
@pytest.mark.client_portal
@pytest.mark.evaluation_url
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_evaluators_dropdown(driver):
    LoginPage.login_recruiter(
        driver,
        "/c/p/candidates/assessments/495562/video/1178191/9"
        "/?current_view=response",
    )
    driver.switch_frame(Candidates.iframe, delay=120)
    time.sleep(5)
    driver.wait_until_element_visible(Candidates.ratings, delay=120)
    driver.click(Candidates.evaluators_dropdown)
    driver.type_keys(Candidates.search_bar, "Alex")
    driver.wait_until_element_visible(Candidates.alex_evaluator)


@pytest.mark.narrow_modal
@pytest.mark.client_portal
@pytest.mark.evaluation_url
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_narrow_modal(driver):
    LoginPage.login_recruiter(
        driver,
        "/c/p/candidates/assessments/518451/video/1206500/9"
        "/?current_view=response",
    )
    driver.switch_frame(Candidates.iframe, delay=120)
    time.sleep(5)
    with pytest.raises(Exception) as excinfo:
        driver.wait_until_element_visible(Candidates.ratings, delay=20)
    unable = "not visible in"
    exception = str(excinfo)
    assert exception.find(unable)


@pytest.mark.one_assigned
@pytest.mark.client_portal
@pytest.mark.evaluation_url
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_one_assigned(driver):
    LoginPage.login_recruiter(
        driver, "/c/p/candidates/assessments/591836/video/1266744/"
    )
    driver.wait_until_element_visible(
        Candidates.evaluators_checkboxes, delay=120
    )
    evaluators_checkboxes = driver.return_elements(
        Candidates.evaluators_checkboxes
    )
    evaluators_checkboxes[5].click()
    driver.click(Candidates.apply_assigned_evaluator)
    driver.wait_until_element_visible(Candidates.apply_assigned_evaluator)
    time.sleep(2)
    not_started = driver.return_elements(Candidates.not_started_evaluation)
    assert len(not_started) == 2
    evaluators_checkboxes[5].click()
    driver.click(Candidates.apply_assigned_evaluator)


@pytest.mark.two_assigned
@pytest.mark.client_portal
@pytest.mark.evaluation_url
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_two_assigned(driver):
    LoginPage.login_recruiter(
        driver, "/c/p/candidates/assessments/561336/video/1241779/"
    )
    driver.wait_until_element_visible(
        Candidates.evaluators_checkboxes, delay=120
    )
    evaluators_checkboxes = driver.return_elements(
        Candidates.evaluators_checkboxes
    )
    evaluators_checkboxes[2].click()
    driver.click(Candidates.apply_assigned_evaluator)
    driver.wait_until_element_visible(Candidates.apply_assigned_evaluator)
    time.sleep(2)
    not_started = driver.return_elements(Candidates.not_started_evaluation)
    in_progress = driver.return_elements(Candidates.in_progress_evaluation)
    assert len(not_started) == 2
    assert len(in_progress) == 1
    evaluators_checkboxes[2].click()
    driver.click(Candidates.apply_assigned_evaluator)


@pytest.mark.one_completed
@pytest.mark.client_portal
@pytest.mark.evaluation_url
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_one_completed(driver):
    LoginPage.login_recruiter(
        driver, "/c/p/candidates/assessments/561338/video/1241780"
    )
    evaluators_checkboxes = driver.return_elements(
        Candidates.evaluators_checkboxes
    )
    driver.wait_until_element_visible(
        Candidates.evaluators_checkboxes, delay=120
    )
    evaluators_checkboxes[2].click()
    driver.click(Candidates.apply_assigned_evaluator)
    driver.wait_until_element_visible(Candidates.apply_assigned_evaluator)
    time.sleep(3)
    # Need some time to load
    not_started = driver.return_elements(Candidates.not_started_evaluation)
    submitted = driver.return_elements(Candidates.submitted_evaluation)
    assert len(not_started) == 2
    assert len(submitted) == 1
    evaluators_checkboxes[2].click()
    driver.click(Candidates.apply_assigned_evaluator)


@pytest.mark.scored_assignment
@pytest.mark.candidates
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_scored_assignment(driver):
    LoginPage.login_recruiter(
        driver, "/c/p/candidates/assessments/521746/video/1209126/"
    )
    driver.wait_until_element_visible(
        Candidates.unavailable_checkbox, delay=120
    )


@pytest.mark.remove_evaluator
@pytest.mark.candidates
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_remove_evaluator(driver):
    LoginPage.login_recruiter(
        driver, "/c/p/candidates/assessments/591795/video/1266714/"
    )
    driver.wait_until_element_visible(
        Candidates.evaluators_checkboxes, delay=120
    )
    evaluators_checkboxes = driver.return_elements(
        Candidates.evaluators_checkboxes
    )
    evaluators_checkboxes[10].click()
    driver.click(Candidates.apply_assigned_evaluator)
    driver.wait_until_element_visible(Candidates.cancel_removing, delay=120)


@pytest.mark.member_self_assignment_on
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_member_self_assignment_on(driver):
    LoginPage.cp_member(
        driver, "/c/p/candidates/assessments/604625/video/1277359"
    )
    driver.wait_until_element_visible(
        Candidates.evaluators_checkboxes, delay=60
    )
    time.sleep(2)
    evaluators = driver.find_elements(
        By.CSS_SELECTOR, Candidates.evaluators_checkboxes["selector"]
    )
    evaluators[16].click()
    driver.click(Candidates.apply_assigned_evaluator)
    time.sleep(3)
    not_started = driver.find_elements(
        By.XPATH, Candidates.not_started_evaluation["selector"]
    )
    assert len(not_started) == 5
    evaluators[16].click()
    driver.click(Candidates.apply_assigned_evaluator)


@pytest.mark.member_self_assignment_off
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_member_self_assignment_off(driver):
    LoginPage.cp_member(
        driver, "/c/p/candidates/assessments/565866/video/1245400/"
    )
    driver.wait_until_element_visible(
        Candidates.evaluators_checkboxes, delay=60
    )
    time.sleep(2)
    evaluators = driver.find_elements(
        By.CSS_SELECTOR, Candidates.evaluators_checkboxes["selector"]
    )
    evaluators[2].click()
    with pytest.raises(Exception) as excinfo:
        driver.click(Candidates.apply_assigned_evaluator)
    unable = "is not clickable at point"
    exception = str(excinfo)
    assert exception.find(unable)
    time.sleep(3)
    not_started = driver.find_elements(
        By.XPATH, Candidates.not_started_evaluation["selector"]
    )
    assert len(not_started) == 1
