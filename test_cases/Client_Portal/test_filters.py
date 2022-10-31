import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.client_portal.candidates import Candidates
from tests.ui_tests.pages.client_portal.filters import Filters
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys


@pytest.mark.filters_status
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_status(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Filters.status, delay=120)
    driver.click(Filters.filters_dropdown)
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, Filters.filters_status_checkboxes['selector'])
    checkboxes_text = driver.find_elements(
        By.CSS_SELECTOR, Filters.status_checkboxes_text['selector'])
    index = 0
    while index < len(checkboxes):
        checkbox_text = checkboxes_text[index].get_attribute('data-for')
        checkboxes[index].click()
        driver.click(Filters.apply_filters_button)
        driver.wait_until_element_visible(Filters.status)
        status_text = driver.find_elements(
            By.XPATH, Filters.status['selector'])
        if len(status_text) > 0:
            for element in status_text:
                assert element.text == checkbox_text
        driver.click(Filters.filters_dropdown)
        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, Filters.filters_status_checkboxes['selector'])
        checkboxes_text = driver.find_elements(
            By.CSS_SELECTOR, Filters.status_checkboxes_text['selector'])
        checkboxes[index].click()
        index += 1


@pytest.mark.filters_recommendation
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_recommendation(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Filters.status, delay=120)
    driver.click(Filters.filters_dropdown)
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, Filters.filters_recommendation_check['selector'])
    checkboxes_text = driver.find_elements(
        By.CSS_SELECTOR, Filters.recommendation_check_text['selector'])
    index = 0

    while index < len(checkboxes):
        needed_text = checkboxes_text[index].get_attribute('data-for')
        checkboxes[index].click()
        driver.click(Filters.apply_filters_button)
        time.sleep(2)
        recommendation_text = driver.find_elements(
            By.XPATH, Filters.recommendation_text['selector'])
        if len(recommendation_text) > 0:
            for status in recommendation_text:
                assert status.text == needed_text
        driver.click(Filters.filters_dropdown)
        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, Filters.filters_recommendation_check['selector'])
        checkboxes_text = driver.find_elements(
            By.CSS_SELECTOR, Filters.recommendation_check_text['selector'])
        checkboxes[index].click()
        index += 1


@pytest.mark.filters_position
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_position(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Filters.status, delay=120)
    driver.click(Filters.filters_dropdown)
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, Filters.filters_position_check['selector'])
    checkboxes_text = driver.find_elements(
        By.CSS_SELECTOR, Filters.position_check_text['selector'])
    index = 0
    while index < len(checkboxes):
        needed_text = checkboxes_text[index].get_attribute('data-for')
        checkboxes[index].click()
        driver.click(Filters.apply_filters_button)
        time.sleep(2)
        position_text = driver.find_elements(
            By.XPATH, Filters.position_text['selector'])
        if len(position_text) > 0:
            for position in position_text:
                assert position.text == needed_text
        driver.click(Filters.filters_dropdown)
        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, Filters.filters_position_check['selector'])
        checkboxes_text = driver.find_elements(
            By.CSS_SELECTOR, Filters.position_check_text['selector'])
        checkboxes[index].click()
        index += 1


@pytest.mark.filters_invited_by
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_invited_by(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Filters.status, delay=120)
    time.sleep(10)
    driver.click(Filters.filters_dropdown)
    driver.wait_until_element_visible(Filters.search)
    search_line = driver.find_element(By.XPATH, Filters.search['selector'])
    search_line.clear()
    search_line.send_keys('lapkouski')
    driver.click(Filters.alex)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Filters.status)
    emails_needed = driver.find_elements(By.XPATH, Filters.emails['selector'])
    if len(emails_needed) > 0:
        for email in emails_needed:
            assert "Alex" in email.text or "alex" in email.text


@pytest.mark.filters_flagged
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_flagged(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.flagged_check)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Filters.status)
    status = driver.find_elements(By.XPATH, Filters.status['selector'])
    flag = driver.find_elements(By.CSS_SELECTOR, Filters.full_flag['selector'])
    if len(status) > 0:
        assert len(status) == len(flag)


@pytest.mark.filters_archived
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_archived(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.archived_check)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Filters.status, delay=60)
    candidate = Candidates(driver)
    driver.click(candidate.checkbox('3'))
    driver.wait_until_element_visible(Candidates.unarchive_button)


@pytest.mark.filters_invited_date_24h
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_invited_date_24h(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.invited_24h)
    driver.click(Filters.apply_filters_button)
    try:
        driver.wait_until_element_visible(Candidates.empty, delay=5)
    except Exception:
        driver.wait_until_element_visible(Candidates.candidate_row)
        invited = driver.find_elements(By.XPATH, Candidates.invited['selector'])
        index = 0
        while index < len(invited):
            get_date = invited[index]
            date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
            date_difference = datetime.now() - date_parsed
            assert int(date_difference.days) == 0
            index += 1


@pytest.mark.filters_invited_date_7d
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_invited_date_7d(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.invited_7d)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Candidates.candidate_row)
    invited = driver.find_elements(By.XPATH, Candidates.invited['selector'])
    index = 0
    if len(invited) > 0:
        while index < len(invited):
            get_date = invited[index]
            date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
            date_difference = datetime.now() - date_parsed
            assert int(date_difference.days) <= 7
            index += 1


@pytest.mark.filters_invited_date_30d
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_invited_date_30d(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Filters.status, delay=120)
    invited = driver.find_elements(By.XPATH, Candidates.invited['selector'])
    index = 0
    while index < len(invited):
        get_date = invited[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 30
        index += 1
    pages = driver.find_elements(By.XPATH,
                                      Candidates.number_of_pages['selector'])
    pages[-1].click()
    time.sleep(2)
    # Need some more time to load
    invited = driver.find_elements(By.XPATH, Candidates.invited['selector'])
    index = 0
    while index < len(invited):
        get_date = invited[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 30
        index += 1


@pytest.mark.filters_invited_date_12m
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_invited_date_12m(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.invited_12m)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Candidates.candidate_row)
    invited = driver.find_elements(By.XPATH, Candidates.invited['selector'])
    index = 0
    while index < len(invited):
        get_date = invited[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 366
        index += 1
    pages = driver.find_elements(By.XPATH,
                                  Candidates.number_of_pages['selector'])
    pages[-1].click()
    time.sleep(2)
    # Need some more time to load
    invited = driver.find_elements(By.XPATH, Candidates.invited['selector'])
    index = 0
    while index < len(invited):
        get_date = invited[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 366
        index += 1


@pytest.mark.filters_invited_date_custom_valid
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=3)
def test_filters_invited_date_custom_valid(driver):
    Filters.disable_invited_30d(driver)
    Filters.input_valid_date(driver)
    driver.wait_until_element_visible(Candidates.invited)
    invited = driver.find_elements(By.XPATH, Candidates.invited['selector'])
    index = 0
    if len(invited ) > 0:
        while index < len(invited ):
            get_date = invited[index]
            assert get_date.text == "05/01/2020" \
                   or get_date.text == "05/02/2020"
            index += 1


@pytest.mark.filters_invited_date_custom_same_date
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_invited_date_custom_same_date(driver):
    Filters.disable_invited_30d(driver)
    Filters.input_same_date(driver)
    driver.wait_until_element_visible(Candidates.invited)
    invited_date = driver.find_elements(By.XPATH, Candidates.invited['selector'])
    index = 0
    while index < len(invited_date):
        get_date = invited_date[index]
        assert get_date.text == "05/01/2020"
        index += 1


@pytest.mark.filters_invited_date_custom_wrong_date
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_invited_date_custom_wrong_date(driver):
    Filters.disable_invited_30d(driver)
    Filters.input_wrong_date(driver)
    driver.wait_until_element_visible(Candidates.empty)


@pytest.mark.filters_completed_date_24h
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_completed_date_24h(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.completed_24h)
    driver.click(Filters.apply_filters_button)
    try:
        driver.wait_until_element_visible(Candidates.empty, delay=5)
    except Exception:
        driver.wait_until_element_visible(Candidates.candidate_row)
        completed = driver.find_elements(By.XPATH,
                                          Candidates.completed['selector'])
        index = 0
        while index < len(completed):
            get_date = completed[index]
            date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
            date_difference = datetime.now() - date_parsed
            assert int(date_difference.days) == 0
            index += 1


@pytest.mark.filters_completed_date_7d
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_completed_date_7d(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.completed_7d)
    driver.click(Filters.apply_filters_button)
    try:
        driver.wait_until_element_visible(Candidates.empty, delay=5)
    except Exception:
        driver.wait_until_element_visible(Candidates.completed)
        completed = driver.find_elements(By.XPATH,
                                     Candidates.completed['selector'])
        index = 0
        while index < len(completed):
            get_date = completed[index]
            date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
            date_difference = datetime.now() - date_parsed
            assert int(date_difference.days) <= 7
            index += 1


@pytest.mark.filters_completed_date_30d
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_completed_date_30d(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.completed_30d)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Filters.recommendation_text)
    completed = driver.find_elements(By.XPATH,
                                     Candidates.completed['selector'])
    index = 0
    while index < len(completed):
        get_date = completed[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 30
        index += 1


@pytest.mark.filters_completed_date_12m
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_filters_completed_date_12m(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.completed_12m)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Filters.recommendation_text)
    completed = driver.find_elements(By.XPATH,
                                     Candidates.completed['selector'])
    index = 0
    while index < len(completed):
        get_date = completed[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 366
        index += 1
    pages = driver.find_elements(By.XPATH,
                                 Candidates.number_of_pages['selector'])
    pages[-1].click()
    time.sleep(2)
    # Need some more time to load
    completed = driver.find_elements(By.XPATH,
                                     Candidates.completed['selector'])
    index = 0
    while index < len(completed):
        get_date = completed[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 366
        index += 1


@pytest.mark.filters_completed_date_custom_valid
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=3)
def test_filters_completed_date_custom_valid(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.completed_custom)
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
    driver.wait_until_element_visible(Candidates.completed)
    completed = driver.find_elements(By.XPATH,
                                     Candidates.completed['selector'])
    index = 0
    if len(completed) > 0:
        while index < len(completed):
            get_date = completed[index]
            assert get_date.text == "05/01/2020" \
                   or get_date.text == "05/02/2020"
            index += 1


@pytest.mark.filters_completed_date_custom_same_date
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=3)
def test_filters_completed_date_custom_same_date(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Filters.status, delay=120)
    driver.click(Filters.filters_dropdown)
    driver.wait_until_element_visible(Filters.recommendation_text)
    time.sleep(3)
    # Need some more time to load
    driver.click(Filters.completed_custom)
    dates_input = driver.find_elements(By.CSS_SELECTOR,
                                       Filters.dates_input_field['selector'])
    today = datetime.now()
    today_format = today.strftime("%m/%d/%Y")
    dates_input[1].send_keys(Keys.BACKSPACE * 10)
    dates_input[1].send_keys(today_format)
    dates_input[1].send_keys(Keys.RETURN)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Candidates.empty)


@pytest.mark.filters_completed_date_custom_wrong_date
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=3)
def test_filters_completed_date_custom_wrong_date(driver):
    Filters.disable_invited_30d(driver)
    driver.click(Filters.completed_custom)
    dates_input = driver.find_elements(By.CSS_SELECTOR,
                                       Filters.dates_input_field['selector'])
    dates_input[0].send_keys(Keys.BACKSPACE * 10)
    dates_input[0].send_keys("08/01/2020")
    dates_input[1].click()
    dates_input[1].clear()
    dates_input[1].send_keys(Keys.BACKSPACE * 10)
    dates_input[1].send_keys("05/02/2020")
    dates_input[1].send_keys(Keys.RETURN)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Candidates.empty)


@pytest.mark.interview_filters_status
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filters_status(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Filters.status, delay=120)
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status)
    driver.click(Filters.filters_dropdown)
    time.sleep(3)
    # Need some more time to load
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, Filters.filters_status_checkboxes['selector'])
    checkboxes_text = driver.find_elements(
        By.CSS_SELECTOR, Filters.status_checkboxes_text['selector'])
    index = 0
    while index < len(checkboxes):
        checkbox_text = checkboxes_text[index].get_attribute('data-for')
        checkboxes[index].click()
        driver.click(Filters.apply_filters_button)
        driver.wait_until_element_visible(Candidates.interviews_status)
        status_text = driver.find_elements(
            By.CSS_SELECTOR, Candidates.interviews_status['selector'])
        if len(status_text) > 0:
            for element in status_text:
                assert element.text == checkbox_text
        driver.click(Filters.filters_dropdown)
        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, Filters.filters_status_checkboxes['selector'])
        checkboxes_text = driver.find_elements(
            By.CSS_SELECTOR, Filters.status_checkboxes_text['selector'])
        checkboxes[index].click()
        index += 1


@pytest.mark.interview_filters_positions
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filters_positions(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Filters.status, delay=120)
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status)
    driver.click(Filters.filters_dropdown)
    time.sleep(3)
    # Need some more time to load
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, Filters.interview_position_check['selector'])
    checkboxes_text = driver.find_elements(
        By.CSS_SELECTOR, Filters.interview_position['selector'])
    index = 0
    while index < len(checkboxes):
        needed_text = checkboxes_text[index].get_attribute('data-for')
        checkboxes[index].click()
        driver.click(Filters.apply_filters_button)
        try:
            driver.wait_until_element_visible(Candidates.empty, delay=5)
        except Exception:
            position_text = driver.find_elements(
                By.XPATH, Candidates.interview_position_text['selector'])
            for position in position_text:
                assert position.text == needed_text \
                       or position.text == "Demo Project test org"
        # One of the games names doesn't match
        driver.click(Filters.filters_dropdown)
        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, Filters.interview_position_check['selector'])
        checkboxes_text = driver.find_elements(
            By.CSS_SELECTOR, Filters.interview_position['selector'])
        checkboxes[index].click()
        index += 1


@pytest.mark.interview_filters_evaluators
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filters_evaluators(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Filters.status, delay=120)
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status)
    driver.click(Filters.filters_dropdown)
    driver.wait_until_element_visible(Filters.pymetrics_evaluator)
    time.sleep(2)
    # Giving extra time
    evaluators_search = driver.find_element(
        By.CSS_SELECTOR, Filters.evaluators_input['selector'])
    evaluators_search.send_keys("Fedor")
    evaluators_search.send_keys(Keys.RETURN)
    driver.click(Filters.fedor_garin)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Candidates.interview_position_text)
    time.sleep(10)
    # Giving extra time to load
    candidates = driver.find_elements(
        By.XPATH, Candidates.interview_position_text['selector'])
    assert len(candidates) == 6


@pytest.mark.interview_filters_evaluations
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filters_evaluations(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Filters.status, delay=120)
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status)
    driver.click(Filters.filters_dropdown)
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, Filters.evaluation_status_check['selector'])
    checkboxes_text = driver.find_elements(
        By.CSS_SELECTOR, Filters.evaluation_status['selector'])
    index = 0
    while index < len(checkboxes):
        needed_text = checkboxes_text[index].get_attribute('data-for')
        checkboxes[index].click()
        driver.click(Filters.apply_filters_button)
        try:
            driver.wait_until_element_visible(Candidates.empty, delay=5)
        except Exception:
            driver.wait_until_element_visible(Candidates.interviews_status)
            time.sleep(3)
            # Needs more time to load
            candidates = driver.find_elements(
                By.XPATH, Candidates.interview_position_text['selector'])
            candidate_index = 0
            while candidate_index < len(candidates):
                candidates[candidate_index].click()
                driver.wait_until_element_visible(Candidates.evaluators)
                evaluators = driver.find_elements(
                    By.CSS_SELECTOR, Candidates.evaluators['selector'])
                py_index = 0
                while py_index < len(evaluators):
                    evaluator = evaluators[py_index]
                    if evaluator.text == "Py Metrics":
                        evaluation_statuses = driver.find_elements(
                            By.CSS_SELECTOR, Candidates.evaluation['selector'])
                        evaluation = evaluation_statuses[py_index]
                        if evaluation.text == needed_text:
                            py_index += 1
                        elif evaluation.text != needed_text:
                            assert evaluation.text == "Not Evaluator"
                            py_index += 1
                    else:
                        py_index += 1
                candidate_index += 1
        driver.click(Filters.filters_dropdown)
        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, Filters.evaluation_status_check['selector'])
        checkboxes_text = driver.find_elements(
            By.CSS_SELECTOR, Filters.evaluation_status['selector'])
        checkboxes[index].click()
        index += 1


@pytest.mark.interview_filters_evaluators_continued
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filters_evaluators_continued(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Filters.status, delay=120)
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.interviews_status)
    driver.click(Filters.filters_dropdown)
    evaluators = driver.find_elements(
        By.CSS_SELECTOR, Filters.evaluators_list['selector'])
    assert len(evaluators) == 5
    assert evaluators[0].text == "Py Metrics"
    assert evaluators[4].text == "Unassigned"


@pytest.mark.interview_filter_24h
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filter_24h(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    Candidates.disable_invited_30_days_interview(driver)
    driver.click(Filters.invited_24h)
    driver.click(Filters.apply_filters_button)
    try:
        driver.wait_until_element_visible(Candidates.empty, delay=5)
    except Exception:
        driver.wait_until_element_visible(Candidates.candidate_row)
        invited = driver.find_elements(By.XPATH,
                                       Candidates.interview_invited['selector'])
        index = 0
        while index < len(invited):
            get_date = invited[index]
            date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
            date_difference = datetime.now() - date_parsed
            assert int(date_difference.days) == 0
            index += 1


@pytest.mark.interview_filter_7d
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filter_7d(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    Candidates.disable_invited_30_days_interview(driver)
    driver.click(Filters.invited_24h)
    driver.click(Filters.apply_filters_button)
    try:
        driver.wait_until_element_visible(Candidates.empty, delay=10)
    except Exception:
        driver.wait_until_element_visible(Candidates.candidate_row)
        invited = driver.find_elements(By.XPATH,
                                       Candidates.interview_invited['selector'])
        index = 0
        while index < len(invited):
            get_date = invited[index]
            date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
            date_difference = datetime.now() - date_parsed
            assert int(date_difference.days) <= 7
            index += 1


@pytest.mark.interview_filter_30d
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filter_30d(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    driver.wait_until_element_visible(Candidates.candidate_row)
    driver.click(Candidates.interviews_tab)
    driver.wait_until_element_visible(Candidates.candidate_row)
    invited = driver.find_elements(By.XPATH, Candidates.interview_invited['selector'])
    index = 0
    while index < len(invited):
        get_date = invited[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 30
        index += 1
    pages = driver.find_elements(By.XPATH,
                                 Candidates.number_of_pages['selector'])
    pages[-1].click()
    time.sleep(2)
    # Need some more time to load
    invited = driver.find_elements(By.XPATH,
                                   Candidates.interview_invited['selector'])
    index = 0
    while index < len(invited):
        get_date = invited[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 30
        index += 1


@pytest.mark.interview_filter_12m
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filter_12m(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    Candidates.disable_invited_30_days_interview(driver)
    driver.click(Filters.invited_12m)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Candidates.candidate_row)
    invited = driver.find_elements(By.XPATH,
                                   Candidates.interview_invited['selector'])
    index = 0
    while index < len(invited):
        get_date = invited[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 366
        index += 1
    pages = driver.find_elements(By.XPATH,
                                 Candidates.number_of_pages['selector'])
    pages[-1].click()
    time.sleep(2)
    # Need some more time to load
    invited = driver.find_elements(By.XPATH, Candidates.interview_invited['selector'])
    index = 0
    while index < len(invited):
        get_date = invited[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 366
        index += 1


@pytest.mark.interview_filter_custom_valid
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filter_custom_valid(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    Candidates.disable_invited_30_days_interview(driver)
    Filters.input_valid_date(driver)
    driver.wait_until_element_visible(Candidates.interview_invited)
    invited = driver.find_elements(By.XPATH, Candidates.interview_invited['selector'])
    index = 0
    while index < len(invited):
        get_date = invited[index]
        assert get_date.text == "05/01/2020" \
                or get_date.text == "05/02/2020"
        index += 1


@pytest.mark.interview_filter_custom_same_date
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filter_custom_same_date(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    Candidates.disable_invited_30_days_interview(driver)
    Filters.input_same_date(driver)
    driver.wait_until_element_visible(Candidates.interview_invited)
    invited = driver.find_elements(By.XPATH, Candidates.interview_invited['selector'])
    index = 0
    while index < len(invited):
        get_date = invited[index]
        assert get_date.text == "05/01/2020"
        index += 1


@pytest.mark.interview_filter_custom_wrong_date
@pytest.mark.client_portal
@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_interview_filter_custom_wrong_date(driver):
    LoginPage.login_recruiter(driver, '/c/p/candidates')
    Candidates.disable_invited_30_days_interview(driver)
    Filters.input_wrong_date(driver)
    driver.wait_until_element_visible(Candidates.empty)
