import pytest
import random

from tests.ui_tests.pages.create_account_page import CreateAccountPage
from tests.ui_tests.pages.privacy_page import PrivacyPage
from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.client_portal.incumbents import Incumbent
from tests.ui_tests.pages.games_application_page import GamesApplicationPage
from tests.ui_tests.pages.client_portal.candidates import Candidates
from tests.ui_tests.pages.client_portal.filters import Filters
from tests.ui_tests.utils import configs
from selenium.webdriver.common.by import By
import time


@pytest.mark.incumbents
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_incumbents_view_label(driver):
    LoginPage.login_recruiter(driver, "/c/p/incumbents")
    driver.wait_until_element_visible(Candidates.testorg_logo)
    driver.wait_until_element_visible(Incumbent.label_text, delay=120)
    label = driver.return_text(Incumbent.label_text)
    assert label == "Label"


@pytest.mark.incumbents
@pytest.mark.client_portal
@pytest.mark.twenty_five_rows_default
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_incumbents_page_shows_with_at_least_25_rows_default(driver):
    LoginPage.login_recruiter(driver, "/c/p/incumbents")
    # looks for "Data Collection" in the incumbent table, to be improved later
    driver.wait_until_element_visible(Candidates.testorg_logo, delay=120)
    driver.wait_until_element_visible(Incumbent.default_label, delay=120)
    table_rows = driver.return_elements(Incumbent.incumbents_checkbox)
    # Default pagination is 25, test count checkboxes we have additional
    # select all checkbox on the column header, so we add a plus one
    count = len(table_rows)
    assert count == 25


@pytest.mark.incumbents
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_change_of_pagination_on_the_incumbents_table(driver):
    LoginPage.login_recruiter(driver, "/c/p/incumbents")
    driver.wait_until_element_visible(Incumbent.label_text, delay=120)
    driver.wait_until_element_visible(Incumbent.default_label, delay=120)
    table_rows = driver.return_elements(Incumbent.incumbents_checkbox)
    # Default pagination is 25, test count checkboxes we have additional
    # select all checkbox on the column header, so we add a plus one
    count = len(table_rows)
    assert count == 25

    driver.wait_until_element_visible(Incumbent.twenty_five_items_per_page)
    driver.click(Incumbent.twenty_five_items_per_page)
    driver.wait_until_element_visible(Incumbent.fifty_items_per_page)
    driver.click(Incumbent.fifty_items_per_page)
    driver.wait_until_element_visible(Incumbent.default_label, delay=120)
    table_rows = driver.return_elements(Incumbent.incumbents_checkbox)
    # Default pagination is 50, test count checkboxes we have additional
    # select all checkbox on the column header, so we add a plus one
    count = len(table_rows)
    assert count == 50


@pytest.mark.incumbents
@pytest.mark.whitelist
@pytest.mark.client_portal
@pytest.mark.C1118373
@pytest.mark.incumbents_whitelist
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_incumbents_whitelist(driver):
    random_num = random.randint(1, 9 ** 11)
    email = "test_automation+test" + str(random_num) + "@example.com"

    LoginPage.login_recruiter(driver, "/c/p/incumbents")
    driver.wait_until_element_visible(Candidates.testorg_logo, delay=120)
    driver.wait_until_element_visible(Incumbent.label_text, delay=120)
    driver.click(Incumbent.whitelist_button)
    driver.click(Incumbent.position_dropdown)
    driver.wait_until_element_visible(Incumbent.active_position, delay=120)
    driver.click(Incumbent.active_position)
    driver.type_keys(Incumbent.email_textbox, email)
    driver.click(Incumbent.submit_button)
    time.sleep(5)
    link = driver.return_text(Incumbent.invite_link)
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
    time.sleep(7)
    privacy_page.click_consent_all()
    privacy_page.submit_consent()
    driver.wait_until_element_visible(
        GamesApplicationPage.action_items_complete_games_button, delay=120
    )


@pytest.mark.incumbents
@pytest.mark.incumbents_status_filter
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_incumbents_status_filter(driver):
    LoginPage.login_recruiter(driver, "/c/p/incumbents")
    driver.wait_until_element_visible(Filters.status, delay=120)
    driver.click(Incumbent.filters_dropdown)
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, Incumbent.filters_status_checkboxes["selector"]
    )
    checkboxes_text = driver.find_elements(
        By.CSS_SELECTOR, Incumbent.status_checkboxes_text["selector"]
    )
    index = 0
    while index < len(checkboxes):
        checkbox_text = checkboxes_text[index].get_attribute("data-for")
        checkboxes[index].click()
        driver.click(Filters.apply_filters_button)
        driver.wait_until_element_visible(Filters.status)
        status_text = driver.find_elements(
            By.XPATH, Filters.status["selector"]
        )
        if len(status_text) > 0:
            for element in status_text:
                assert element.text == checkbox_text
        driver.click(Incumbent.filters_dropdown)
        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, Incumbent.filters_status_checkboxes["selector"]
        )
        checkboxes_text = driver.find_elements(
            By.CSS_SELECTOR, Incumbent.status_checkboxes_text["selector"]
        )
        checkboxes[index].click()
        index += 1


@pytest.mark.incumbents
@pytest.mark.position_filter_incumbents
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_position_filter(driver):
    LoginPage.login_recruiter(driver, "/c/p/incumbents")
    driver.wait_until_element_visible(Filters.status, delay=120)
    time.sleep(5)
    # This page needs more time
    driver.click(Incumbent.filters_dropdown)
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, Incumbent.filters_position_check["selector"]
    )
    checkboxes_text = driver.find_elements(
        By.CSS_SELECTOR, Incumbent.position_check_text["selector"]
    )
    index = 0
    while index < len(checkboxes):
        checkbox_text = checkboxes_text[index].get_attribute("data-for")
        checkboxes[index].click()
        driver.click(Filters.apply_filters_button)
        try:
            driver.wait_until_element_visible(Filters.status, delay=3)
        except Exception:
            position_text = driver.find_elements(
                By.XPATH, Filters.position_text["selector"]
            )
            for element in position_text:
                assert element.text == checkbox_text
        driver.click(Incumbent.filters_dropdown)
        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, Incumbent.filters_position_check["selector"]
        )
        checkboxes_text = driver.find_elements(
            By.CSS_SELECTOR, Incumbent.position_check_text["selector"]
        )
        checkboxes[index].click()
        index += 1


@pytest.mark.incumbents
@pytest.mark.incumbents_search
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_incumbents_search(driver):
    LoginPage.login_recruiter(driver, "/c/p/incumbents")
    driver.wait_until_element_visible(Filters.status, delay=120)
    driver.type_keys(Incumbent.incumbent_search, "fedtestinc\n")
    driver.wait_until_element_visible(Incumbent.fedtestinc_user)


@pytest.mark.incumbents
@pytest.mark.incumbents_career_growth_tab
@pytest.mark.client_portal
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_incumbents_career_growth_tab(driver):
    LoginPage.login_recruiter(driver, "/c/p/incumbents")
    driver.wait_until_element_visible(Filters.status, delay=120)
    time.sleep(2)
    # Giving some extra time to load
    incumbents = driver.find_elements(
        By.CSS_SELECTOR, Incumbent.incumbents["selector"]
    )
    incumbents[5].click()
    driver.wait_until_element_visible(Incumbent.career_growth_tab, delay=120)
    driver.click(Incumbent.career_growth_tab)
    driver.wait_until_element_visible(Incumbent.no_positions_text)
