import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.marketplace_page import MarketplacePage

import tests.ui_tests.utils.configs as configs


@pytest.mark.xfail
@pytest.mark.C998301
@pytest.mark.csv_secret
@pytest.mark.matches
@pytest.mark.marketplace
def test_setup_user_with_no_matches(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_user_with_no_matches'
    )
    driver.visit('C998301', secret)
    driver.click(MarketplacePage.join_the_marketplace_btn)
    LoginPage.login_without_given_csv_user(
        driver, secret['username'], secret['password'])
    driver.wait_until_element_visible(
        MarketplacePage.match_loading_page_close_btn)
    driver.click(MarketplacePage.match_loading_page_close_btn)
    driver.wait_until_element_visible(
        MarketplacePage.complete_action_items_header)


@pytest.mark.xfail
@pytest.mark.C984006
@pytest.mark.csv_secret
@pytest.mark.matches
@pytest.mark.marketplace
def test_setup_marketplace_user_with_matches(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_marketplace_user_with_matches'
    )
    driver.visit('C984006', secret)
    driver.click(MarketplacePage.join_the_marketplace_btn)
    LoginPage.login_without_given_csv_user(
        driver, secret['username'], secret['password'])
    driver.wait_until_element_visible(MarketplacePage.client_matches_list)
    driver.click(MarketplacePage.client_matches_close_btn)
    driver.wait_until_element_visible(MarketplacePage.matches_card_list)
    driver.wait_until_element_visible(MarketplacePage.filter_section)


@pytest.mark.C984004
@pytest.mark.csv_secret
@pytest.mark.matches
@pytest.mark.marketplace
def test_setup_incomplete_user_with_transfer_invitation(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_incomplete_user_with_transfer_invitation'
    )
    driver.visit('C984004', secret)
    driver.click(MarketplacePage.join_the_marketplace_btn)
    LoginPage.login_without_given_csv_user(
        driver, secret['username'], secret['password'])
    driver.wait_until_element_visible(MarketplacePage.pymetrics_logo)
    driver.wait_until_element_visible(MarketplacePage.error_message)
    driver.wait_until_element_visible(MarketplacePage.please_contact_msg)


@pytest.mark.xfail  # can't get passed the skills section for onboarding
@pytest.mark.C984147
@pytest.mark.csv_secret
@pytest.mark.matches
@pytest.mark.marketplace
def test_setup_complete_user_with_transfer_invitation(secretFixture, driverFixture):  # noqa
    ts = secretFixture
    driver = driverFixture
    secret = ts.get_secret(
        'setup_complete_user_with_transfer_invitation'
    )
    driver.visit('C984147', secret)
    driver.click(MarketplacePage.join_the_marketplace_btn)
    LoginPage.login_without_given_csv_user(
        driver, secret['username'], secret['password'])
    driver.wait_until_element_visible(MarketplacePage.education_dropdown)
    driver.click(MarketplacePage.education_dropdown)
    driver.click(MarketplacePage.high_school_option)
    driver.click(MarketplacePage.graduation_year_dropdown)
    driver.click(MarketplacePage.graduation_year_2002_option)
    driver.type_keys(
        MarketplacePage.current_location_textbox, 'New York')
    cities = driver.return_elements(MarketplacePage.realtime_city_matches)
    assert len(cities) == 2
    driver.click(MarketplacePage.active_realtime_city_match)
    driver.click(MarketplacePage.submit_button)
    driver.wait_until_element_visible(MarketplacePage.match_loading_page)
