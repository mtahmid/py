import os
import pytest
import time

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.development_reports import DevelopmentReports
from selenium.webdriver.common.by import By

import tests.ui_tests.utils.configs as configs


@pytest.mark.dev_report
@pytest.mark.dev_report_contributor
@pytest.mark.client_portal
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_dev_report_contributor(driver):
    LoginPage.login_dev_report_contributor(driver, '/results/development/')
    driver.wait_until_element_visible(DevelopmentReports.dev_report_download)
    driver.navigate_to(
        configs.url + '/results/downloads/development_reports/?as=html')
    time.sleep(3)
    driver.wait_until_element_visible(DevelopmentReports.development_report_header)
    driver.return_element(DevelopmentReports.header_logo)
    dates = driver.find_elements(By.CSS_SELECTOR,
                                DevelopmentReports.development_report_headers['selector'])
    date = dates[1]
    assert date.text == "February 1, 2021"
    name = driver.find_element(By.XPATH,
                                DevelopmentReports.development_report_name['selector'])
    assert name.text == "Alex Test"
    driver.return_element(DevelopmentReports.about_this_report)
    driver.return_element(DevelopmentReports.overview)
    driver.return_element(DevelopmentReports.interpreting)
    driver.return_element(DevelopmentReports.summary_title)
    driver.return_element(DevelopmentReports.summary_text)
    driver.return_element(DevelopmentReports.legend)
    driver.return_element(DevelopmentReports.factors_section)
    driver.return_element(DevelopmentReports.summary_factor)
    driver.return_element(DevelopmentReports.quartile)
    driver.return_element(DevelopmentReports.factor_title)
    driver.return_element(DevelopmentReports.factor_details)

@pytest.mark.dev_report
@pytest.mark.dev_report_leadership
@pytest.mark.client_portal
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_dev_report_leadership(driver):
    LoginPage.login_dev_report_leadership(driver, '/results/development/')
    driver.wait_until_element_visible(DevelopmentReports.dev_report_download)
    driver.navigate_to(
        configs.url + '/results/downloads/development_reports/?as=html')
    time.sleep(3)
    driver.wait_until_element_visible(DevelopmentReports.development_report_header)
    driver.return_element(DevelopmentReports.header_logo)
    dates = driver.find_elements(By.CSS_SELECTOR,
                                DevelopmentReports.development_report_headers['selector'])
    date = dates[1]
    assert date.text == "February 2, 2021"
    name = driver.find_element(By.XPATH,
                                DevelopmentReports.development_report_name['selector'])
    assert name.text == "Alex Test"
    driver.return_element(DevelopmentReports.leadership_report)
    driver.return_element(DevelopmentReports.about_this_report)
    driver.return_element(DevelopmentReports.overview)
    driver.return_element(DevelopmentReports.interpreting)
    driver.return_element(DevelopmentReports.summary_title)
    driver.return_element(DevelopmentReports.summary_text)
    driver.return_element(DevelopmentReports.legend)
    driver.return_element(DevelopmentReports.factors_section)
    driver.return_element(DevelopmentReports.summary_factor)
    driver.return_element(DevelopmentReports.quartile)
    driver.return_element(DevelopmentReports.factor_title)
    driver.return_element(DevelopmentReports.factor_details)
