import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.client_portal.admin import Admin
from tests.ui_tests.pages.client_portal.dashboard import Dashboard

import tests.ui_tests.utils.configs as configs
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.cp_admin
@pytest.mark.client_portal
def test_admin_button(driver):
    LoginPage.login_recruiter(driver, '/c/p')
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + '/c/p/administration/memberships')
    user = driver.return_text(Admin.user_row_title)
    assert user == 'User'


@pytest.mark.cp_admin
@pytest.mark.client_portal
def test_interviews_settings(driver):
    LoginPage.login_recruiter(driver, '/c/p')
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + '/c/p/administration/memberships')
    driver.click(Admin.interviews_settings)
    add_interview = driver.return_text(Admin.add_interview_button)
    assert add_interview == 'Add Interview'


@pytest.mark.cp_admin
@pytest.mark.client_portal
def test_video_styles_settings(driver):
    LoginPage.login_recruiter(driver, '/c/p')
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + '/c/p/administration/memberships')
    driver.wait_until_element_visible(Admin.styles_and_branding_settings)
    driver.click(Admin.styles_and_branding_settings)
    driver.wait_until_element_visible(Admin.login_preview_button)


@pytest.mark.cp_admin
@pytest.mark.cp_admin_interview
@pytest.mark.client_portal
@pytest.mark.published_toggle
@pytest.mark.regression_no_csv
@pytest.mark.regression
@pytest.mark.flaky(reruns=2)
def test_published_video_toggles(driver):
    admin_page = Admin(driver)

    LoginPage.login_recruiter(driver, '/c/p/administration/interviews/12/setup')
    driver.wait_until_element_visible(admin_page.interview_toggle('2'), delay=60)
    toggle_postion_1 = driver.return_attribute(
        admin_page.interview_toggle('2'), 'outerHTML')
    driver.click(admin_page.interview_toggle('2'))
    toggle_postion_2 = driver.return_attribute(
        admin_page.interview_toggle('2'), 'outerHTML')
    assert toggle_postion_1 == toggle_postion_2


@pytest.mark.cp_admin
@pytest.mark.cp_admin_interview
@pytest.mark.client_portal
@pytest.mark.flaky(reruns=2)
def test_unpublished_video_toggles(driver):
    admin_page = Admin(driver)

    LoginPage.login_recruiter(driver, '/c/p/administration/interviews/45/setup')
    driver.wait_until_element_visible(admin_page.interview_toggle('2'), delay=60)
    toggle_postion_1 = driver.return_attribute(
        admin_page.interview_toggle('2'), 'outerHTML')
    driver.click(admin_page.interview_toggle('2'))
    toggle_postion_2 = driver.return_attribute(
        admin_page.interview_toggle('2'), 'outerHTML')
    assert toggle_postion_1 != toggle_postion_2


@pytest.mark.duplicate_interview
@pytest.mark.regression_no_csv
@pytest.mark.regression
@pytest.mark.flaky(reruns=2)
def test_duplicate_interview(driver):
    admin_page = Admin(driver)
    LoginPage.login_recruiter(driver, '/c/p/administration/interviews')
    driver.wait_until_element_visible(Admin.duplicate_icon, delay=120)
    duplicate_icon = driver.find_elements(
        By.CSS_SELECTOR, Admin.duplicate_icon['selector'])
    duplicate_icon[1].click()
    driver.wait_until_element_visible(Admin.select_placeholder, delay=120)
    driver.click(Admin.select_placeholder)
    driver.wait_until_element_visible(Admin.position_ten, delay=120)
    driver.click(Admin.position_ten)
    driver.click(Admin.duplicate_button)
    driver.wait_until_element_visible(admin_page.interview_toggle('2'), delay=120)
    driver.click(Admin.questions_tab)
    driver.wait_until_element_visible(Admin.type_question, delay=120)
    question_field = driver.find_element(
        By.CSS_SELECTOR, Admin.type_question['selector'])
    question_field.clear()
    question_field.send_keys('Automated question')
    time.sleep(1)
    driver.click(Admin.add_question)
    driver.wait_until_element_visible(Admin.automated_question, delay=120)
    time.sleep(2)
    # Giving some extra time
    remove_icon = driver.find_elements(
        By.XPATH, Admin.remove_interview['selector'])
    remove_icon[-1].click()
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(3)
    # Giving some extra time
    icon_new = driver.find_elements(
        By.XPATH, Admin.remove_interview['selector'])
    assert len(remove_icon) == len(icon_new) + 1
    icon_new[0].click()
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(6)
    # Giving some extra time
    duplicate_icon_new = driver.find_elements(
            By.CSS_SELECTOR, Admin.duplicate_icon['selector'])
    assert len(duplicate_icon) == len(duplicate_icon_new)


@pytest.mark.regression_no_csv
@pytest.mark.regression
@pytest.mark.contributor_toggle
@pytest.mark.flaky(reruns=2)
def test_contributor_toggle(driver):
    LoginPage.login_recruiter(driver, '/c/p/administration/development-reports')
    driver.wait_until_element_visible(Admin.dev_report_toggle, delay=120)
    driver.click(Admin.dev_report_toggle)
    time.sleep(1)
    text = driver.find_element(By.CSS_SELECTOR,
                               Admin.toggle_text['selector'])
    assert text.text == "No, employees should not access their own reports"
    driver.click(Admin.save_button)
    driver.wait_until_element_visible(Admin.check_mark, delay=120)
    driver.click(Admin.dev_report_toggle)
    driver.click(Admin.save_button)
    driver.wait_until_element_visible(Admin.check_mark, delay=120)
    assert text.text == "Yes, give employees direct access their own reports"


@pytest.mark.regression_no_csv
@pytest.mark.regression
@pytest.mark.leadership_toggle
@pytest.mark.flaky(reruns=2)
def test_leadership_toggle(driver):
    LoginPage.login_recruiter(driver, '/c/p/administration/development-reports')
    driver.wait_until_element_visible(Admin.dev_report_toggle, delay=120)
    driver.click(Admin.leadership_subtab)
    driver.click(Admin.dev_report_toggle)
    time.sleep(1)
    text = driver.find_element(By.CSS_SELECTOR,
                               Admin.toggle_text['selector'])
    assert text.text == "No, employees should not access their own reports"
    driver.click(Admin.save_button)
    driver.wait_until_element_visible(Admin.check_mark, delay=120)
    driver.click(Admin.dev_report_toggle)
    driver.click(Admin.save_button)
    driver.wait_until_element_visible(Admin.check_mark, delay=120)
    assert text.text == "Yes, give employees direct access their own reports"


@pytest.mark.regression_no_csv
@pytest.mark.regression
@pytest.mark.position_templates_same_name
@pytest.mark.flaky(reruns=2)
def test_position_templates_same_name(driver):
    LoginPage.login_recruiter(driver, '/c/p/administration/position-templates/candidates')
    driver.wait_until_element_visible(Admin.create_position_template, delay=120)
    driver.click(Admin.create_position_template)
    time.sleep(2)
    # Giving an extra time to load
    position_name = driver.find_element(
        By.CSS_SELECTOR, Admin.position_name['selector'])
    position_name.send_keys('Pymetrics Default Template')
    time.sleep(2)
    # Giving an extra time to load
    driver.click(Admin.save_button)
    driver.wait_until_element_visible(Admin.warning)
