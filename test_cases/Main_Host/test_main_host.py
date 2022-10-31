import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.main_host_page import MainPage

import tests.ui_tests.utils.configs as configs


@pytest.mark.C898312
@pytest.mark.smoke
@pytest.mark.production
@pytest.mark.main_page
def test_main_external_landing_page(driver):
    driver.navigate_to(configs.url)
    driver.click(MainPage.solutionsTab)
    driver.wait_until_element_visible(MainPage.solutionsHeroBackground)
    driver.click(MainPage.candidatesTab)
    driver.wait_until_element_visible(MainPage.candidatesHeroBackground)
