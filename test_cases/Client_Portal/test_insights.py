import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.client_portal.admin import Admin
from tests.ui_tests.pages.client_portal.workforce_insights import \
    WorkforceInsights
from selenium.webdriver.common.by import By

import tests.ui_tests.utils.configs as configs
import time


@pytest.mark.insights_page
@pytest.mark.flaky(reruns=2)
@pytest.mark.workforce
@pytest.mark.regression_no_csv
def test_insights_page(driver):
    LoginPage.login_recruiter(driver, '/c/p/insights/MO/internal-mobility')
    driver.wait_until_element_visible(WorkforceInsights.iframe, delay=120)
    driver.switch_frame(WorkforceInsights.iframe)

@pytest.mark.workforce_attributes
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.workforce
@pytest.mark.flaky(reruns=2)
def test_workforce_attributes(driver):
    LoginPage.login_recruiter(driver, '/c/p/insights/WO/workforce-dna')
    driver.wait_until_element_visible(WorkforceInsights.iframe, delay=60)
    driver.switch_frame(WorkforceInsights.iframe)
    time.sleep(5)
    driver.wait_until_element_visible(WorkforceInsights.clusters, delay=60)
    attributes = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.attributes_checkboxes['selector'])
    attributes[1].click()
    time.sleep(20)
    # It takes a very long time to load
    circles = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.factor_circles['selector'])
    assert len(circles) == 48


@pytest.mark.workforce_filter_role
@pytest.mark.regression
@pytest.mark.workforce
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_workforce_filter_role(driver):
    LoginPage.login_recruiter(driver, '/c/p/insights/WO/workforce-dna')
    driver.wait_until_element_visible(WorkforceInsights.iframe, delay=60)
    driver.switch_frame(WorkforceInsights.iframe)
    time.sleep(5)
    driver.wait_until_element_visible(WorkforceInsights.clusters, delay=60)
    toggles = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.filter_toggles['selector'])
    toggles[0].click()
    time.sleep(3)
    clusters = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.clusters['selector'])
    cluster_before = len(clusters)
    checkboxes = driver.find_elements(
        By.XPATH, WorkforceInsights.filters_checkboxes['selector'])
    checkboxes[0].click()
    time.sleep(4)
    clusters = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.clusters['selector'])
    cluster_after = len(clusters)
    assert cluster_after < cluster_before


@pytest.mark.workforce_sort
@pytest.mark.regression
@pytest.mark.workforce
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_workforce_sort(driver):
    LoginPage.login_recruiter(driver, '/c/p/insights/WO/workforce-dna')
    driver.wait_until_element_visible(WorkforceInsights.iframe, delay=60)
    driver.switch_frame(WorkforceInsights.iframe)
    time.sleep(5)
    # Needs extra time
    driver.wait_until_element_visible(WorkforceInsights.clusters, delay=60)
    clusters = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.clusters['selector'])
    clusters_positions = clusters[0].get_attribute('style')
    driver.click(WorkforceInsights.sort_by_dropdown)
    time.sleep(2)
    # Needs extra time
    driver.click(WorkforceInsights.sort_by_count)
    time.sleep(2)
    # Needs extra time
    clusters_positions_sorted = clusters[0].get_attribute('style')
    assert clusters_positions != clusters_positions_sorted


@pytest.mark.workforce_sort_by_role
@pytest.mark.regression
@pytest.mark.workforce
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_workforce_cluster_by_role(driver):
    LoginPage.login_recruiter(driver, '/c/p/insights/WO/workforce-dna')
    driver.wait_until_element_visible(WorkforceInsights.iframe, delay=60)
    driver.switch_frame(WorkforceInsights.iframe)
    time.sleep(5)
    # Needs extra time
    driver.wait_until_element_visible(WorkforceInsights.clusters, delay=60)
    clusters = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.clusters['selector'])
    driver.click(WorkforceInsights.cluster_by_dropdown)
    time.sleep(2)
    # Needs extra time
    driver.click(WorkforceInsights.cluster_by_position_title)
    time.sleep(20)
    # Needs extra time, it takes around 20 sec to load
    clusters_filtered = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.clusters['selector'])
    assert len(clusters) != len(clusters_filtered)


@pytest.mark.workforce_grid
@pytest.mark.regression
@pytest.mark.workforce
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_workforce_grid(driver):
    LoginPage.login_recruiter(driver, '/c/p/insights/WO/workforce-dna')
    driver.wait_until_element_visible(WorkforceInsights.iframe, delay=60)
    driver.switch_frame(WorkforceInsights.iframe)
    time.sleep(5)
    # Needs extra time
    driver.wait_until_element_visible(WorkforceInsights.clusters, delay=60)
    clusters = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.clusters['selector'])
    clusters_positions = clusters[0].get_attribute('style')
    driver.click(WorkforceInsights.grid)
    time.sleep(2)
    # Needs extra time
    clusters_positions_sorted = clusters[0].get_attribute('style')
    assert clusters_positions != clusters_positions_sorted


@pytest.mark.clusters_comparison
@pytest.mark.regression
@pytest.mark.workforce
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_clusters_comparison(driver):
    LoginPage.login_recruiter(driver, '/c/p/insights/WO/workforce-dna')
    driver.wait_until_element_visible(WorkforceInsights.iframe, delay=60)
    driver.switch_frame(WorkforceInsights.iframe)
    time.sleep(5)
    # Needs extra time
    driver.wait_until_element_visible(WorkforceInsights.clusters, delay=60)
    clusters = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.clusters['selector'])
    clusters[0].click()
    time.sleep(2)
    # Giving extra time for animation
    clusters[5].click()
    driver.wait_until_element_visible(WorkforceInsights.vs)


@pytest.mark.capabilities
@pytest.mark.regression
@pytest.mark.workforce
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_capabilities(driver):
    LoginPage.login_recruiter(driver, '/c/p/insights/WO/workforce-dna')
    driver.wait_until_element_visible(WorkforceInsights.iframe, delay=120)
    driver.switch_frame(WorkforceInsights.iframe)
    time.sleep(5)
    # Needs extra time
    driver.wait_until_element_visible(WorkforceInsights.clusters, delay=120)
    driver.click(WorkforceInsights.capabilities_dropdown)
    driver.wait_until_element_visible(WorkforceInsights.capabilities_option)
    driver.click(WorkforceInsights.capabilities_option)
    time.sleep(2)
    # Some extra time for loading
    driver.wait_until_element_visible(WorkforceInsights.different_capabilties)
    clusters = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.clusters['selector'])
    clusters_positions = clusters[0].get_attribute('style')
    capabilities = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.different_capabilties['selector'])
    capabilities[0].click()
    time.sleep(2)
    # Giving time for animation
    clusters_positions_sorted = clusters[0].get_attribute('style')
    assert clusters_positions != clusters_positions_sorted


@pytest.mark.manipulating_data
@pytest.mark.workforce
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_manipulating_data(driver):
    LoginPage.login_recruiter(driver, '/c/p/administration/insights/')
    driver.wait_until_element_visible(Admin.manager_flag, delay=120)
    switches = driver.find_elements(By.CSS_SELECTOR, Admin.switches['selector'])
    switches[41].click()
    time.sleep(2)
    driver.navigate_to('https://staging.pymetrics.com/c/p/insights/WO/workforce-dna')
    driver.wait_until_element_visible(WorkforceInsights.iframe, delay=120)
    driver.switch_frame(WorkforceInsights.iframe)
    time.sleep(2)
    # Needs extra time
    driver.wait_until_element_visible(WorkforceInsights.clusters, delay=120)
    driver.click(WorkforceInsights.cluster_by_dropdown)
    time.sleep(2)
    driver.click(WorkforceInsights.cluster_by_manager)
    time.sleep(5)
    clusters = driver.find_elements(
        By.CSS_SELECTOR, WorkforceInsights.clusters['selector'])
    assert len(clusters) == 1
    driver.navigate_to('https://staging.pymetrics.com/c/p/administration/insights/')
    driver.wait_until_element_visible(Admin.switches, delay=120)
    time.sleep(3)
    switches = driver.find_elements(By.CSS_SELECTOR, Admin.switches['selector'])
    switches[41].click()
    time.sleep(2)
