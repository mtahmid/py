import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.client_portal.recruiter_report import RecruiterReport
from tests.ui_tests.pages.client_portal.dashboard import Dashboard
from tests.ui_tests.pages.client_portal.candidates import Candidates

import tests.ui_tests.utils.configs as configs


@pytest.mark.recruiter_report
@pytest.mark.client_portal
def test_html_recruiter_report(driver):
    LoginPage.login_recruiter(driver, '/c/p')
    driver.return_element(Dashboard.high_chart)
    driver.navigate_to(
        configs.url + '/c/p/candidates/assessments/577391/games')
    report_html = driver.return_attribute(
        Candidates.recruiter_report_download_button, 'href')
    driver.navigate_to(report_html + '&as=html')
    driver.wait_until_element_visible(RecruiterReport.report_body)
    driver.return_element(RecruiterReport.header)
    driver.return_element(RecruiterReport.header_content)
    driver.return_element(RecruiterReport.score)
    driver.return_element(RecruiterReport.model_factors)
