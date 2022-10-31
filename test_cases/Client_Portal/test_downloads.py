import pytest

from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.client_portal.downloads import Downloads
from tests.ui_tests.pages.client_portal.dashboard import Dashboard

import tests.ui_tests.utils.configs as configs


@pytest.mark.downloads
@pytest.mark.client_portal
def test_downloads_button(driver):
    LoginPage.login_recruiter(driver, '/c/p')
    driver.wait_until_element_visible(Dashboard.high_chart)
    driver.navigate_to(configs.url + '/c/p/downloads')
    file_name = driver.return_text(Downloads.file_name_row_title)
    assert file_name == 'File Name'
