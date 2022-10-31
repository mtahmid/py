import string
import time
import pytest

from pymetrics.utils import random
from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.client_portal.positions import Positions
from tests.ui_tests.pages.client_portal.candidates import Candidates

import tests.ui_tests.utils.configs as configs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.position_card
@pytest.mark.positions
@pytest.mark.client_portal
@pytest.mark.regression_no_csv
@pytest.mark.regression
@pytest.mark.flaky(reruns=2)
def test_position_card(driver):
    LoginPage.login_recruiter(driver, "/c/p/positions/37")
    driver.wait_until_element_visible(Positions.assessment, delay=120)
    driver.wait_until_element_visible(Positions.candidate_link)


@pytest.mark.positions
@pytest.mark.client_portal
@pytest.mark.positions_filter_by_status
@pytest.mark.regression_no_csv
@pytest.mark.regression
@pytest.mark.flaky(reruns=2)
def test_positions_filter_by_status(driver):
    LoginPage.login_recruiter(driver, "/c/p/positions")
    driver.wait_until_element_visible(Positions.positions_statuses, delay=120)
    time.sleep(15)
    # This page has an extra loading icon
    driver.click(Positions.position_more_filters)
    filters_checkboxes = driver.find_elements(
        By.CSS_SELECTOR, Positions.positions_filters_checkboxes["selector"]
    )
    filters_checkboxes[0].click()
    driver.click(Positions.position_apply_filters)
    time.sleep(12)
    position_status = driver.find_elements(
        By.XPATH, Positions.single_status["selector"]
    )
    for status in position_status:
        assert status.text == "Published"
    driver.click(Positions.position_more_filters)
    filters_checkboxes = driver.find_elements(
        By.CSS_SELECTOR, Positions.positions_filters_checkboxes["selector"]
    )
    filters_checkboxes[0].click()
    filters_checkboxes[1].click()
    driver.click(Positions.position_apply_filters)
    time.sleep(12)
    position_status = driver.find_elements(
        By.XPATH, Positions.single_status["selector"]
    )
    for status in position_status:
        assert status.text == "Unpublished"


@pytest.mark.positions
@pytest.mark.client_portal
@pytest.mark.positions_per_page
@pytest.mark.regression_no_csv
@pytest.mark.regression
@pytest.mark.flaky(reruns=2)
def test_positions_per_page(driver):
    LoginPage.login_recruiter(driver, "/c/p/positions")
    driver.wait_until_element_visible(Positions.positions_statuses, delay=120)
    time.sleep(15)
    # This page has an extra loading icon
    driver.click(Candidates.items_per_page_dropdown)
    driver.click(Candidates.ten_items_per_page)
    time.sleep(7)
    number_of_positions = driver.find_elements(
        By.CSS_SELECTOR, Positions.positions_statuses["selector"]
    )
    assert len(number_of_positions) <= 10


@pytest.mark.positions
@pytest.mark.client_portal
@pytest.mark.positions_search
@pytest.mark.regression_no_csv
@pytest.mark.regression
@pytest.mark.flaky(reruns=2)
def test_positions_search(driver):
    LoginPage.login_recruiter(driver, "/c/p/positions")
    driver.wait_until_element_visible(Positions.positions_statuses, delay=120)
    time.sleep(15)
    driver.type_keys(Positions.search_field, "test position alex")
    search_field = driver.find_element(
        By.CSS_SELECTOR, Positions.search_field["selector"]
    )
    search_field.send_keys(Keys.RETURN)
    time.sleep(3)
    number_of_positions = driver.find_elements(
        By.CSS_SELECTOR, Positions.positions_statuses["selector"]
    )
    assert len(number_of_positions) == 1
<<<<<<< HEAD


@pytest.mark.positions
@pytest.mark.client_portal
@pytest.mark.positions_template_creation
@pytest.mark.regression_no_csv
@pytest.mark.regression
@pytest.mark.flaky(reruns=2)
def test_positions_add_a_position(driver):
    random_num = random.randint(1, 9 ** 11)
    positionTemplateName = 'Test Position' + str(random_num)

    LoginPage.login_recruiter(driver, '/c/p/positions')
    driver.wait_until_element_visible(Positions.positions_statuses, delay=120)
    time.sleep(15)
    driver.click(Positions.add_a_position_button)
    driver.type_keys(
        Positions.position_name_field, positionTemplateName)
    time.sleep(3)
    driver.click(Positions.save_position_button)
