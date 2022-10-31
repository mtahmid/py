from tests.ui_tests.pages.base_page import BasePage


class SettingsPage(BasePage):
    account_dropdown = {
        'description': 'Profile dropdown menu button',
        'selector': '#dropdown-menu-container'
    }
    change_password = {
        'description': 'Change password button',
        'selector': '//button[contains(text(), "Change Password")]',
        'type': 'xpath'
    }
    old_password = {
        'description': 'Old password field',
        'selector': '#id_old_password'
    }
    new_password = {
        'description': 'New password field',
        'selector': '#id_new_password1'
    }
    new_password_again = {
        'description': 'New password again field',
        'selector': '#id_new_password2'
    }
    submit = {
        'description': 'Submit button',
        'selector': '.submit-button'
    }
    success_change = {
        'description': 'Successful change text',
        'selector': '//h3[contains(text(), "Password change successful!")]',
        'type': 'xpath'
    }
    continue_button = {
        'description': 'Continue button',
        'selector': '//a[contains(text(), "Continue")]',
        'type': 'xpath'
    }
    account_dropdown_settings = {
        'description': 'Settings button in the profile dropdown',
        'selector': '#header-nav-settings'
    }
    account_settings_button = {
        'description': 'Account settings button in "Your Settings"',
        'selector': '#account-settings-nav'
    }
    account_language_dropdown = {
        'description': 'Language dropdown',
        'selector': '.dropdown.fa.fa-angle-down'
    }
    language_dropdown_arabic = {
        'description': 'Language dropdown Arabic',
        'selector': '//*[contains(text(), "العربية")]',
        'type': 'xpath'
    }
    your_settings_arabic = {
        'description': 'Your Settings text in Arabic',
        'selector': '//*[contains(text(), "إعداداتك")]',
        'type': 'xpath'
    }
    language_dropdown_chinese = {
        'description': 'Language dropdown 繁體中文',
        'selector': '//*[contains(text(), "繁體中文")]',
        'type': 'xpath'
    }
    your_settings_chinese = {
        'description': 'Your Settings text in 繁體中文',
        'selector': '//*[contains(text(), "你的設定")]',
        'type': 'xpath'
    }
    language_dropdown_french = {
        'description': 'Language dropdown French',
        'selector': '//*[contains(text(), "Français")]',
        'type': 'xpath'
    }
    your_settings_french = {
        'description': 'Your Settings text in French',
        'selector': '//*[contains(text(), "Vos paramètres")]',
        'type': 'xpath'
    }
    language_dropdown_german = {
        'description': 'Language dropdown German',
        'selector': '//*[contains(text(), "Deutsche")]',
        'type': 'xpath'
    }
    your_settings_german = {
        'description': 'Your Settings text in German',
        'selector': '//*[contains(text(), "Ihre Einstellungen")]',
        'type': 'xpath'
    }
    language_dropdown_greek = {
        'description': 'Language dropdown Greek',
        'selector': '//*[contains(text(), "Ελληνικά")]',
        'type': 'xpath'
    }
    your_settings_greek = {
        'description': 'Your Settings text in Greek',
        'selector': '//*[contains(text(), "Οι ρυθμίσεις σας")]',
        'type': 'xpath'
    }
    language_dropdown_indonesian = {
        'description': 'Language dropdown Indonesian',
        'selector': '//*[contains(text(), "Bahasa Indonesia")]',
        'type': 'xpath'
    }
    your_settings_indonesian = {
        'description': 'Your Settings text in Indonesian',
        'selector': '//*[contains(text(), "Pengaturan Anda")]',
        'type': 'xpath'
    }
    language_dropdown_italian = {
        'description': 'Language dropdown Italian',
        'selector': '//*[contains(text(), "Italiano")]',
        'type': 'xpath'
    }
    your_settings_italian = {
        'description': 'Your Settings text in Italian',
        'selector': '//*[contains(text(), "Le tue impostazioni")]',
        'type': 'xpath'
    }
    language_dropdown_japanese = {
        'description': 'Language dropdown Japanese',
        'selector': '//*[contains(text(), "日本語")]',
        'type': 'xpath'
    }
    your_settings_japanese = {
        'description': 'Your Settings text in Japanese',
        'selector': '//*[contains(text(), "個人設定")]',
        'type': 'xpath'
    }
    language_dropdown_korean = {
        'description': 'Language dropdown Korean',
        'selector': '//*[contains(text(), "한국어")]',
        'type': 'xpath'
    }
    your_settings_korean = {
        'description': 'Your Settings text in Korean',
        'selector': '//*[contains(text(), "설정")]',
        'type': 'xpath'
    }
    language_dropdown_mongolian = {
        'description': 'Language dropdown Mongolian',
        'selector': '//*[contains(text(), "Монгол хэл")]',
        'type': 'xpath'
    }
    your_settings_mongolian = {
        'description': 'Your Settings text in Mongolian',
        'selector': '//*[contains(text(), "Таны тохиргоо")]',
        'type': 'xpath'
    }
    language_dropdown_polish = {
        'description': 'Language dropdown Polish',
        'selector': '//*[contains(text(), "język polski")]',
        'type': 'xpath'
    }
    your_settings_polish = {
        'description': 'Your Settings text in Polish',
        'selector': '//*[contains(text(), "Twoje ustawienia")]',
        'type': 'xpath'
    }
    language_dropdown_portuguese = {
        'description': 'Language dropdown Portuguese',
        'selector': '//*[contains(text(), "Português")]',
        'type': 'xpath'
    }
    your_settings_portuguese = {
        'description': 'Your Settings text in Portuguese',
        'selector': '//*[contains(text(), "As suas definições")]',
        'type': 'xpath'
    }
    language_dropdown_portuguese_brazil = {
        'description': 'Language dropdown Portuguese (Brazil)',
        'selector': '//*[contains(text(), "Português – Brasil")]',
        'type': 'xpath'
    }
    your_settings_portuguese_brazil = {
        'description': 'Your Settings text in Portuguese (Brazil)',
        'selector': '//*[contains(text(), "Suas configurações")]',
        'type': 'xpath'
    }
    language_dropdown_simplified_chinese = {
        'description': 'Language dropdown 中文',
        'selector': '//*[contains(text(), "中文")]',
        'type': 'xpath'
    }
    your_settings_simplified_chinese = {
        'description': 'Your Settings text in 中文',
        'selector': '//*[contains(text(), "您的设置")]',
        'type': 'xpath'
    }
    language_dropdown_spanish = {
        'description': 'Language dropdown Spanish',
        'selector': '//*[contains(text(), "Español")]',
        'type': 'xpath'
    }
    your_settings_spanish = {
        'description': 'Your Settings text in Spanish',
        'selector': '//*[contains(text(), "Tu configuración")]',
        'type': 'xpath'
    }
    language_dropdown_spanish_latin_america = {
        'description': 'Language dropdown Spanish (Latin America)',
        'selector': '//*[contains(text(), "Español de América Latina")]',
        'type': 'xpath'
    }
    your_settings_spanish_latin_america = {
        'description': 'Your Settings text in Spanish (Latin America)',
        'selector': '//*[contains(text(), "Sus ajustes")]',
        'type': 'xpath'
    }
    language_dropdown_thai = {
        'description': 'Language dropdown Thai',
        'selector': '//*[contains(text(), "ภาษาไทย")]',
        'type': 'xpath'
    }
    your_settings_thai = {
        'description': 'Your Settings text in Thai',
        'selector': '//*[contains(text(), "การตั้งค่าของคุณ")]',
        'type': 'xpath'
    }
    language_dropdown_turkish = {
        'description': 'Language dropdown Turkish',
        'selector': '//*[contains(text(), "Türkçe")]',
        'type': 'xpath'
    }
    your_settings_turkish = {
        'description': 'Your Settings text in Turkish',
        'selector': '//*[contains(text(), "Ayarlarınız")]',
        'type': 'xpath'
    }
    language_dropdown_vietnamese = {
        'description': 'Language dropdown Vietnamese',
        'selector': '//*[contains(text(), "Tiếng Việt")]',
        'type': 'xpath'
    }
    your_settings_vietnamese = {
        'description': 'Your Settings text in Vietnamese',
        'selector': '//*[contains(text(), "Cài đặt của bạn")]',
        'type': 'xpath'
    }
    language_dropdown_nederlands = {
        'description': 'Language dropdown Nederlands',
        'selector': '//*[contains(text(), "Nederlands")]',
        'type': 'xpath'
    }
    your_settings_nederlands = {
        'description': 'Your Settings text in Nederlands',
        'selector': '//*[contains(text(), "Uw instellingen")]',
        'type': 'xpath'
    }
    language_dropdown_english = {
        'description': 'Language dropdown English',
        'selector': '//*[contains(text(), "English")]',
        'type': 'xpath'
    }
    your_settings_english = {
        'description': 'Your Settings text in English',
        'selector': '//*[contains(text(), "Your Settings")]',
        'type': 'xpath'
    }
    language_dropdown_romanian = {
        'description': 'Language dropdown Romanian',
        'selector': '//*[contains(text(), "Română")]',
        'type': 'xpath'
    }
    your_settings_romanian = {
        'description': 'Your Settings text in Romanian',
        'selector': '//*[contains(text(), "Setările dvs.")]',
        'type': 'xpath'
    }
    language_dropdown_danish = {
        'description': 'Language dropdown Romanian',
        'selector': '//*[contains(text(), "dansk")]',
        'type': 'xpath'
    }
    your_settings_danish = {
        'description': 'Your Settings text in Romanian',
        'selector': '//*[contains(text(), "Dine indstillinger")]',
        'type': 'xpath'
    }
    language_dropdown_russian = {
        'description': 'Language dropdown Romanian',
        'selector': '//*[contains(text(), "Русский")]',
        'type': 'xpath'
    }
    your_settings_russian = {
        'description': 'Your Settings text in Romanian',
        'selector': '//*[contains(text(), "Ваши настройки")]',
        'type': 'xpath'
    }
    language_dropdown_ukrainian = {
        'description': 'Language dropdown Romanian',
        'selector': '//*[contains(text(), "Українська")]',
        'type': 'xpath'
    }
    your_settings_ukrainian = {
        'description': 'Your Settings text in Romanian',
        'selector': '//*[contains(text(), "Ваші налаштування")]',
        'type': 'xpath'
    }
    language_dropdown_finnish = {
        'description': 'Language dropdown Romanian',
        'selector': '//*[contains(text(), "Suomen kieli")]',
        'type': 'xpath'
    }
    your_settings_finnish = {
        'description': 'Your Settings text in Romanian',
        'selector': '//*[contains(text(), "Omat asetukset")]',
        'type': 'xpath'
    }
    language_dropdown_swedish = {
        'description': 'Language dropdown Romanian',
        'selector': '//*[contains(text(), "Svenska")]',
        'type': 'xpath'
    }
    your_settings_swedish = {
        'description': 'Your Settings text in Romanian',
        'selector': '//*[contains(text(), "Dina inställningar")]',
        'type': 'xpath'
    }
    language_dropdown_hungarian = {
        'description': 'Language dropdown Romanian',
        'selector': '//*[contains(text(), "Magyar")]',
        'type': 'xpath'
    }
    your_settings_hungarian = {
        'description': 'Your Settings text in Romanian',
        'selector': '//*[contains(text(), "Saját beállítások")]',
        'type': 'xpath'
    }
    language_dropdown_czech = {
        'description': 'Language dropdown Romanian',
        'selector': '//*[contains(text(), "Čeština")]',
        'type': 'xpath'
    }
    your_settings_czech = {
        'description': 'Your Settings text in Romanian',
        'selector': '//*[contains(text(), "Vaše nastavení")]',
        'type': 'xpath'
    }
    change_email_button = {
        'description': 'Change Email Button',
        'selector': '[ng-click="showEmailModal()"]'
    }
    email_update_modal_text = {
        'description': 'Email update modal text',
        'selector': '//*[contains(text(), "Please contact")]',
        'type': 'xpath'
    }
    view_privacy_notice_btn = {
        'description': 'View Privacy Notice Button',
        'selector': '//button[contains(text(), "View Privacy Notice")]',
        'type': 'xpath'
    }
    privacy_nav = {
        'description': 'Privacy Nav Item',
        'selector': '#privacy-settings-nav',
    }
    download_data = {
        'description': 'Download data button',
        'selector': '[download]',
    }
    data_privacy = {
        'description': 'Data privacy button',
        'selector': '[href="/privacy/account/"] button',
    }
    request_data = {
        'description': 'Request data button',
        'selector': '[ng-disabled="gettingData"]',
    }
