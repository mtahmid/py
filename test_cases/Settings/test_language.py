import os
import pytest

import tests.ui_tests.utils.configs as configs
from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.games_page import GamesPage
from tests.ui_tests.pages.settings_page import SettingsPage


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_arabic(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_arabic)
    driver.wait_until_element_visible(SettingsPage.your_settings_arabic)
    arabic_settings = driver.return_text(GamesPage.banner_text)
    assert arabic_settings == 'إعداداتك'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_chinese(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_chinese)
    driver.wait_until_element_visible(SettingsPage.your_settings_chinese)
    chinese_settings = driver.return_text(GamesPage.banner_text)
    assert chinese_settings == '你的設定'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_french(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_french)
    driver.wait_until_element_visible(SettingsPage.your_settings_french)
    french_settings = driver.return_text(GamesPage.banner_text)
    assert french_settings == 'Vos paramètres'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_german(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_german)
    driver.wait_until_element_visible(SettingsPage.your_settings_german)
    german_settings = driver.return_text(GamesPage.banner_text)
    assert german_settings == 'Ihre Einstellungen'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_greek(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_greek)
    driver.wait_until_element_visible(SettingsPage.your_settings_greek)
    greek_settings = driver.return_text(GamesPage.banner_text)
    assert greek_settings == 'Οι ρυθμίσεις σας'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_indonesian(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_indonesian)
    driver.wait_until_element_visible(SettingsPage.your_settings_indonesian)
    indonesian_settings = driver.return_text(GamesPage.banner_text)
    assert indonesian_settings == 'Pengaturan Anda'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_italian(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_italian)
    driver.wait_until_element_visible(SettingsPage.your_settings_italian)
    italian_settings = driver.return_text(GamesPage.banner_text)
    assert italian_settings == 'Le tue impostazioni'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_japanese(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_japanese)
    driver.wait_until_element_visible(SettingsPage.your_settings_japanese)
    japanese_settings = driver.return_text(GamesPage.banner_text)
    assert japanese_settings == '個人設定'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_mongolian(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_mongolian)
    driver.wait_until_element_visible(SettingsPage.your_settings_mongolian)
    mongolian_settings = driver.return_text(GamesPage.banner_text)
    assert mongolian_settings == 'Таны тохиргоо'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_polish(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_polish)
    driver.wait_until_element_visible(SettingsPage.your_settings_polish)
    polish_settings = driver.return_text(GamesPage.banner_text)
    assert polish_settings == 'Twoje ustawienia'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_portuguese(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_portuguese)
    driver.wait_until_element_visible(SettingsPage.your_settings_portuguese)
    portuguese_settings = driver.return_text(GamesPage.banner_text)
    assert portuguese_settings == 'As suas definições'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_portuguese_brazil(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_portuguese_brazil)
    driver.wait_until_element_visible(
        SettingsPage.your_settings_portuguese_brazil)
    portuguese_brazil_settings = driver.return_text(GamesPage.banner_text)
    assert portuguese_brazil_settings == 'Suas configurações'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_simplified_chinese(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_simplified_chinese)
    driver.wait_until_element_visible(
        SettingsPage.your_settings_simplified_chinese)
    simplified_chinese_settings = driver.return_text(GamesPage.banner_text)
    assert simplified_chinese_settings == '您的设置'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_spanish(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_spanish)
    driver.wait_until_element_visible(SettingsPage.your_settings_spanish)
    spanish_settings = driver.return_text(GamesPage.banner_text)
    assert spanish_settings == 'Tu configuración'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_spanish_latin_america(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_spanish_latin_america)
    driver.wait_until_element_visible(
        SettingsPage.your_settings_spanish_latin_america)
    spanish_latin_america_settings = driver.return_text(GamesPage.banner_text)
    assert spanish_latin_america_settings == 'Sus ajustes'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_thai(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_thai)
    driver.wait_until_element_visible(SettingsPage.your_settings_thai)
    thai_settings = driver.return_text(GamesPage.banner_text)
    assert thai_settings == 'การตั้งค่าของคุณ'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_turkish(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_turkish)
    driver.wait_until_element_visible(SettingsPage.your_settings_turkish)
    turkish_settings = driver.return_text(GamesPage.banner_text)
    assert turkish_settings == 'Ayarlarınız'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_vietnamese(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_vietnamese)
    driver.wait_until_element_visible(SettingsPage.your_settings_vietnamese)
    vietnamese_settings = driver.return_text(GamesPage.banner_text)
    assert vietnamese_settings == 'Cài đặt của bạn'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_english(driver):
    LoginPage.login(driver, '/settings')
    english_settings = driver.return_text(GamesPage.banner_text)
    assert english_settings == 'Your Settings'
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_vietnamese)
    driver.wait_until_element_visible(SettingsPage.your_settings_vietnamese)
    vietnamese_settings = driver.return_text(GamesPage.banner_text)
    assert vietnamese_settings == 'Cài đặt của bạn'
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_english)
    driver.wait_until_element_visible(SettingsPage.your_settings_english)
    english_settings = driver.return_text(GamesPage.banner_text)
    assert english_settings == 'Your Settings'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_nederlands(driver):
    LoginPage.login(driver, '/settings')
    english_settings = driver.return_text(GamesPage.banner_text)
    assert english_settings == 'Your Settings'
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_nederlands)
    driver.wait_until_element_visible(SettingsPage.your_settings_nederlands)
    nederlands_settings = driver.return_text(GamesPage.banner_text)
    assert nederlands_settings == 'Uw instellingen'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_korean(driver):
    LoginPage.login(driver, '/settings')
    english_settings = driver.return_text(GamesPage.banner_text)
    assert english_settings == 'Your Settings'
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_korean)
    driver.wait_until_element_visible(SettingsPage.your_settings_korean)
    korean_settings = driver.return_text(GamesPage.banner_text)
    assert korean_settings == '설정'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_romanian(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_romanian)
    driver.wait_until_element_visible(SettingsPage.your_settings_romanian)
    romanian_settings = driver.return_text(GamesPage.banner_text)
    assert romanian_settings == 'Setările dvs.'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_danish(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_danish)
    driver.wait_until_element_visible(SettingsPage.your_settings_danish)
    danish_settings = driver.return_text(GamesPage.banner_text)
    assert danish_settings == 'Dine indstillinger'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_russian(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_russian)
    driver.wait_until_element_visible(SettingsPage.your_settings_russian)
    russian_settings = driver.return_text(GamesPage.banner_text)
    assert russian_settings == 'Ваши настройки'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_ukrainian(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_ukrainian)
    driver.wait_until_element_visible(SettingsPage.your_settings_ukrainian)
    ukrainian_settings = driver.return_text(GamesPage.banner_text)
    assert ukrainian_settings == 'Ваші налаштування'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_finnish(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_finnish)
    driver.wait_until_element_visible(SettingsPage.your_settings_finnish)
    finnish_settings = driver.return_text(GamesPage.banner_text)
    assert finnish_settings == 'Omat asetukset'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_swedish(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_swedish)
    driver.wait_until_element_visible(SettingsPage.your_settings_swedish)
    swedish_settings = driver.return_text(GamesPage.banner_text)
    assert swedish_settings == 'Dina inställningar'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_hungarian(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_hungarian)
    driver.wait_until_element_visible(SettingsPage.your_settings_hungarian)
    hungarian_settings = driver.return_text(GamesPage.banner_text)
    assert hungarian_settings == 'Saját beállítások'


@pytest.mark.C886039
@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.settings
@pytest.mark.language
@pytest.mark.regression
@pytest.mark.regression_no_csv
@pytest.mark.flaky(reruns=2)
def test_settings_language_dropdown_czech(driver):
    LoginPage.login(driver, '/settings')
    driver.click(SettingsPage.account_language_dropdown)
    driver.click(SettingsPage.language_dropdown_czech)
    driver.wait_until_element_visible(SettingsPage.your_settings_czech)
    czech_settings = driver.return_text(GamesPage.banner_text)
    assert czech_settings == 'Vaše nastavení'
