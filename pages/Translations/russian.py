from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.register_page import RegisterPage
from tests.ui_tests.pages.games_page import GamesPage

class Russian(BasePage):
    submit_language = {
        'description': 'Submit the language',
        'selector': '[name="submitAccessibilityLanguage"]',
    }
    submit_game_advice = {
        'description': 'Submit game advice',
        'selector': '[name="consentToIntegrityStatement"]',
    }
    game_advice_russian = {
        'description': 'Header text in Russian',
        'selector': '//h1[contains(text(), "Приступая к играм, вы подтверждаете приведенные ")]',
        'type': 'xpath',
    }
    continue_in_russian = {
        'description': 'Continue button in Russian',
        'selector': '//span[(text() = "Продолжить")]',
        'type': 'xpath',
    }
    money_exchange_instructions_in_russian = {
        'description': 'Instructions in Russian',
        'selector': '//span[contains(text(), "В этом раунде вы будете работать с другим случайным участником.")]',
        'type': 'xpath',
    }
    keypress_instructions_in_russian = {
        'description': 'Instructions in Russian for the Keypress game',
        'selector': '//span[contains(text(), "Сейчас вы увидите обратный отсчет.")]',
        'type': 'xpath',
    }
    keypress_game_space_bar = {
        'description': 'Space bar in Russian',
        'selector': '//span[contains(text(), "пробел")]',
        'type': 'xpath',
    }
    ballons_instructions_in_russian = {
        'description': 'Instructions in Russian for Balloons game',
        'selector': '//span[contains(text(), "В этой игре ваша задача — заработать как можно больше ")]',
        'type': 'xpath',
    }
    left_hand = {
        'description': 'Left hand in Russian',
        'selector': '//span[contains(text(), "Левша")]',
        'type': 'xpath',
    }
    another_ruble_symbol = {
        'description': 'Another selector for Ruble symbol',
        'selector': '.icon-type__money-rub',
    }
    begin_in_russian = {
        'description': 'Begin button in Russian',
        'selector': '//span[(text() = "Начать")]',
        'type': 'xpath',
    }
    play_games_buttons = {
        'description': 'Play games 12 buttons',
        'selector': '//a[contains(text(), "Играть")]',
        'type': 'xpath',
    }
    ruble_symbol = {
        'description': 'Ruble symbol',
        'selector': '//span[contains(text(), "₽")]',
        'type': 'xpath',
    }
    ruble_amount = {
        'description': 'Amount of money',
        'selector': '//span[contains(text(), "800")]',
        'type': 'xpath',
    }

    game1_title = {
        'description': 'Game 1 title in Russian',
        'selector': '//span[contains(text(), "Поздравляем!")]',
        'type': 'xpath',
    }
    balloons_pump = {
        'description': 'Balloons game pump in Russian',
        'selector': '//span[contains(text(), "Надуть")]',
        'type': 'xpath',
    }
    money_exchange2_instructions_in_russian = {
        'description': 'Instructions in Russian for Money exchange 2',
        'selector': '//span[contains(text(), "В этом раунде вы будете работать с другим случайным участником.")]',
        'type': 'xpath',
    }
    money_exchange2_text = {
        'description': 'Money exchange 2 some text',
        'selector': '//span[contains(text(), "Вы только что заработали ")]',
        'type': 'xpath',
    }
    digits_game_instructions_in_russian = {
        'description': 'Instructions in Russian for Digits game',
        'selector': '//span[contains(text(), "Сейчас вам быстро покажут несколько цифр.")]',
        'type': 'xpath',
    }
    digits_game_text = {
        'description': 'Digits game some text',
        'selector': '//span[contains(text(), "Введите показанные цифры и нажмите клавишу")]',
        'type': 'xpath',
    }
    easy_or_hard_instructions_in_russian = {
        'description': 'Instructions in Russian for game Easy or hard',
        'selector': '//span[contains(text(), "В каждом раунде вам нужно выбрать одно из двух заданий ")]',
        'type': 'xpath',
    }
    easy_or_hard_text = {
        'description': 'Easy or hard some text',
        'selector': '//span[contains(text(), "Выберите задание")]',
        'type': 'xpath',
    }
    stop_instructions_in_russian = {
        'description': 'Instructions in Russian for Stop game',
        'selector': '//span[contains(text(), "пробел")]',
        'type': 'xpath',
    }
    cards_instructions_in_russian = {
        'description': 'Instructions in Russian for the Cards game',
        'selector': '//span[contains(text(), "В этой игре ваша задача — выиграть как можно больше денег")]',
        'type': 'xpath',
    }
    cards_text = {
        'description': 'Cards game some text',
        'selector': '//span[contains(text(), "Прибыль")]',
        'type': 'xpath',
    }
    arrows_instructions_in_russian = {
        'description': 'Instructions in Russian for the Arrows game',
        'selector': '//span[contains(text(), "Если стрелки ")]',
        'type': 'xpath',
    }
    length_instructions_in_russian = {
        'description': 'Instructions in Russian for the Length game',
        'selector': '//span[contains(text(), "Сейчас вам будут показывать по одному из двух лиц: ")]',
        'type': 'xpath',
    }
    towers_instructions_in_russian = {
        'description': 'Instructions in Russian for the Towers game',
        'selector': '//span[contains(text(), "Отменить ход")]',
        'type': 'xpath',
    }
    towers_text = {
        'description': 'Towers game some text',
        'selector': '//span[contains(text(), "Очистить все")]',
        'type': 'xpath',
    }
    faces_game_instructions_in_russian = {
        'description': 'Instructions in Russian for Faces game',
        'selector': '//span[contains(text(), "Сейчас вам будут показывать фотографии людей с разными выражениями лиц")]',
        'type': 'xpath',
    }
    faces_game_text = {
        'description': 'Some text at Faces game',
        'selector': '//div[contains(text(), "Отвращение")]',
        'type': 'xpath',
    }
    intro_text = {
        'description': 'Russian text in intro page for the interview',
        'selector': '//h2[contains(text(), "Добро пожаловать на собеседование pymetrics!")]',
        'type': 'xpath',
    }
    introduction_title_in_russian = {
        'description': 'Intro title for the interview',
        'selector': '//a[(text() = "Вступление")]',
        'type': 'xpath',
    }
    about_company_in_russian = {
        'description': 'About company title for the interview',
        'selector': '//a[(text() = "Компания")]',
        'type': 'xpath',
    }
    about_company_text_in_russian = {
        'description': 'About company text for the interview',
        'selector': '//h1[(text() = "Сведения об этой должности")]',
        'type': 'xpath',
    }
    min_russian = {
        'description': 'About company text for the interview',
        'selector': '//div[(text() = "3мин.")]',
        'type': 'xpath',
    }
    what_to_expect = {
        'description': 'What to expect title in Russian',
        'selector': '//a[(text() = "Что вас ожидает")]',
        'type': 'xpath',
    }
    emphasis_text = {
        'description': 'Emphasis text in Russian',
        'selector': '//span[(text() = "но при этом вторая запись будет отправлена автоматически.")]',
        'type': 'xpath',
    }
    setup_text = {
        'description': 'Setup text in Russian',
        'selector': '//h2[(text() = "Проверка оборудования")]',
        'type': 'xpath',
    }
    config_text = {
        'description': 'Config text in Russian',
        'selector': '//h4[(text() = "О проверке")]',
        'type': 'xpath',
    }
    continue_in_russian_interview = {
        'description': 'Continue button in Russian',
        'selector': '//button[(text() = "Продолжить")]',
        'type': 'xpath',
    }
    start_tests_interview = {
        'description': 'Start tests button in Russian',
        'selector': '//button[(text() = "Запустить проверки")]',
        'type': 'xpath',
    }
    select_dropdown_interview = {
        'description': 'Select languages dropdown for the interview',
        'selector': 'select',
    }
    russian_option_interview = {
        'description': 'Russian language for the interview',
        'selector': '//option[(text() = "Русский")]',
        'type': 'xpath',
    }
    configuration_popup = {
        'description': 'Language configuration pop up in Russian',
        'selector': '//div[(text() = "Настройки языка")]',
        'type': 'xpath',
    }

    def getting_to_games(driver):
        LoginPage.login_spanish_user(driver, '/applications/341373/games/games-advice/')
        driver.wait_until_element_visible(RegisterPage.language_dropdown)
        driver.click(RegisterPage.language_dropdown)
        driver.click(RegisterPage.russian_language_option)
        driver.click(Russian.submit_language)
        driver.wait_until_element_visible(Russian.game_advice_russian)
        driver.click(Russian.submit_game_advice)
        driver.click(GamesPage.close_icon)
