import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.marketplace_page import MarketplacePage

from selenium.webdriver.common.by import By
import time


@pytest.mark.login_marketplace
@pytest.mark.marketplace
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_login_marketplace(driver):
    LoginPage.login_user_marketplace(driver, '/login')
    driver.wait_until_element_visible(MarketplacePage.careers, delay=120)
    url = 'https://staging.pymetrics.com/invite/talent-marketplace/'
    driver.navigate_to(url)
    driver.wait_until_element_visible(MarketplacePage.careers, delay=120)


@pytest.mark.recommended_jobs
@pytest.mark.marketplace
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_recommended_jobs(driver):
    LoginPage.login_user_marketplace(driver, '/login')
    driver.wait_until_element_visible(MarketplacePage.careers, delay=120)
    driver.click(MarketplacePage.recommended_jobs)
    driver.wait_until_element_visible(MarketplacePage.complete_action_text, delay=120)
    driver.click(MarketplacePage.complete_action_text)
    driver.wait_until_element_visible(MarketplacePage.complete_games, delay=120)


@pytest.mark.multiple_locations
@pytest.mark.marketplace
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_multiple_locations(driver):
    LoginPage.login_user_marketplace(driver, '/login')
    driver.wait_until_element_visible(MarketplacePage.careers, delay=120)
    driver.click(MarketplacePage.recommended_jobs)
    driver.wait_until_element_visible(MarketplacePage.partner_roles, delay=120)
    driver.click(MarketplacePage.partner_roles)
    driver.wait_until_element_visible(MarketplacePage.multiple_locations)


@pytest.mark.match_filter
@pytest.mark.marketplace
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_match_filter(driver):
    LoginPage.login_user_marketplace(driver, '/login')
    driver.wait_until_element_visible(MarketplacePage.careers, delay=120)
    driver.click(MarketplacePage.filter_dropdown)
    time.sleep(1)
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, MarketplacePage.filter_checkboxes['selector'])
    index = 0
    for check in checkboxes:
        checkboxes[index].click()
        driver.click(MarketplacePage.apply_button)
        time.sleep(2)
        careers_number = driver.find_element(
            By.CSS_SELECTOR, MarketplacePage.careers_number['selector'])
        assert careers_number.text != "64"
        driver.click(MarketplacePage.filter_dropdown)
        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, MarketplacePage.filter_checkboxes['selector'])
        checkboxes[index].click()
        index += 1
    driver.click(MarketplacePage.clear_filter)
    careers_number = driver.find_element(
        By.CSS_SELECTOR, MarketplacePage.careers_number['selector'])
    time.sleep(2)
    assert careers_number.text == "64"


@pytest.mark.user_no_access
@pytest.mark.marketplace
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_user_no_access(driver):
    url = 'https://staging.pymetrics.com/transfer/=cHJvamVjdDozMTg2MA==/'
    driver.navigate_to(url)
    driver.wait_until_element_visible(MarketplacePage.join_the_marketplace_btn, delay=120)
    driver.click(MarketplacePage.join_the_marketplace_btn)
    driver.type_keys(LoginPage.userNameTextBox, "alex.lapkouski+641@pymetrics.com")
    driver.click(LoginPage.next_button)
    driver.type_keys(LoginPage.passwordTextBox, "6428531Vbycr!")
    driver.click(LoginPage.client_portal_login_button)
    driver.wait_until_element_visible(MarketplacePage.ineligible)


@pytest.mark.careers_cards
@pytest.mark.marketplace
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_careers_cards(driver):
    LoginPage.login_user_marketplace(driver, '/login')
    driver.wait_until_element_visible(MarketplacePage.careers, delay=120)
    careers = driver.find_elements(By.CSS_SELECTOR, MarketplacePage.careers['selector'])
    careers[0].click()
    driver.wait_until_element_visible(MarketplacePage.skills, delay=120)
    driver.wait_until_element_visible(MarketplacePage.see_more_courses)
    driver.click(MarketplacePage.open_jobs)
    driver.wait_until_element_visible(MarketplacePage.jobs)
    driver.click(MarketplacePage.courses)
    driver.wait_until_element_visible(MarketplacePage.different_courses)
