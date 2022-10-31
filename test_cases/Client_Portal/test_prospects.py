import pytest
import time

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.client_portal.prospects import Prospects
from tests.ui_tests.pages.client_portal.filters import Filters
from selenium.webdriver.common.by import By


@pytest.mark.prospects
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_prospects_button(driver):
    LoginPage.login_recruiter(driver, "/c/p/prospective-candidates")
    driver.wait_until_element_visible(Prospects.empty, delay=120)
    driver.wait_until_element_visible(Prospects.current_location)


@pytest.mark.prospect_card
@pytest.mark.prospects
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_prospects_card(driver):
    LoginPage.login_recruiter(
        driver, "/c/p/prospective-candidates/147118/matches"
    )
    driver.wait_until_element_visible(Prospects.prospect_email, delay=120)
    driver.wait_until_element_visible(Prospects.prospect_linkedin)
    driver.wait_until_element_visible(Prospects.prospect_resume)
    driver.wait_until_element_visible(Prospects.skills_breakdown)
    driver.wait_until_element_visible(Prospects.fit_details)


@pytest.mark.prospects
@pytest.mark.prospects_filter
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_prospects_filter(driver):
    LoginPage.login_recruiter(driver, "/c/p/prospective-candidates")
    driver.wait_until_element_visible(Prospects.empty, delay=120)
    time.sleep(5)
    driver.click(Prospects.prospects_filter)
    driver.click(Filters.clear_filters)
    driver.wait_until_element_visible(Prospects.prospects_list, delay=120)


@pytest.mark.prospects
@pytest.mark.prospects_filter_flagged
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_prospects_filter_flagged(driver):
    LoginPage.login_recruiter(driver, "/c/p/prospective-candidates")
    driver.wait_until_element_visible(Prospects.empty, delay=120)
    time.sleep(6)
    driver.click(Prospects.prospects_filter)
    driver.click(Filters.flagged_check)
    driver.click(Filters.invited_7d)
    driver.click(Filters.apply_filters_button)
    driver.wait_until_element_visible(Filters.full_flag, delay=120)


@pytest.mark.prospects
@pytest.mark.prospects_filter_position
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_prospects_filter_position(driver):
    LoginPage.login_recruiter(driver, "/c/p/prospective-candidates")
    driver.wait_until_element_visible(Prospects.empty, delay=120)
    time.sleep(6)
    driver.click(Prospects.prospects_filter)
    driver.click(Filters.invited_7d)
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, Prospects.positions_check["selector"]
    )
    checkboxes_text = driver.find_elements(
        By.CSS_SELECTOR, Prospects.positions["selector"]
    )
    index = 1
    while index < len(checkboxes):
        needed_text = checkboxes_text[index].get_attribute("data-for")
        checkboxes[index].click()
        driver.click(Filters.apply_filters_button)
        time.sleep(2)
        position_text = driver.find_elements(
            By.XPATH, Filters.position_text["selector"]
        )
        if len(position_text) > 0:
            for position in position_text:
                assert position.text == needed_text
        driver.click(Prospects.prospects_filter)
        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, Prospects.positions_check["selector"]
        )
        checkboxes_text = driver.find_elements(
            By.CSS_SELECTOR, Prospects.positions["selector"]
        )
        checkboxes[index].click()
        index += 1


@pytest.mark.prospects
@pytest.mark.prospects_filter_location
@pytest.mark.client_portal
@pytest.mark.regression
# @pytest.mark.regression_no_csv
def test_prospects_filter_location(driver):
    LoginPage.login_recruiter(driver, "/c/p/prospective-candidates")
    driver.wait_until_element_visible(Prospects.empty, delay=120)
    time.sleep(7)
    driver.click(Prospects.prospects_filter)
    driver.click(Filters.invited_7d)
    search_line = driver.find_element(
        By.CSS_SELECTOR, Prospects.search_city["selector"]
    )
    search_line.clear()
    search_line.send_keys("New York City")
    driver.click(Prospects.ny_city_location)
    driver.click(Filters.apply_filters_button)
    time.sleep(2)
    prospects = driver.find_elements(
        By.CSS_SELECTOR, Prospects.prospects_list["selector"]
    )
    index = 0
    while index < 25:
        prospects[index].click()
        driver.wait_until_element_visible(
            Prospects.position_location, delay=120
        )
        location = driver.find_element(
            By.CSS_SELECTOR, Prospects.position_location["selector"]
        )
        assert (
            location.text == "New York City, NY"
            or location.text == "Multiple locations"
        )
        index += 1
