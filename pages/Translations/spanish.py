from tests.ui_tests.pages.base_page import BasePage
from tests.ui_tests.pages.login_page import LoginPage
from tests.ui_tests.pages.register_page import RegisterPage
from tests.ui_tests.pages.games_page import GamesPage

class Spanish(BasePage):
    submit_language = {
        'description': 'Submit the language',
        'selector': '[name="submitAccessibilityLanguage"]',
    }
    submit_game_advice = {
        'description': 'Submit game advice',
        'selector': '[name="consentToIntegrityStatement"]',
    }
    game_advice_spanish = {
        'description': 'Header text in Spanish',
        'selector': '//h1[contains(text(), "Si continúas jugando, confirmas que:")]',
        'type': 'xpath',
    }
    continue_in_spanish = {
        'description': 'Continue button in Spanish',
        'selector': '//span[(text() = "Continuar")]',
        'type': 'xpath',
    }
    money_exchange_instructions_in_spanish = {
        'description': 'Instructions in Spanish',
        'selector': '//span[contains(text(), "Para esta prueba, trabajarás con otro participante aleatorio.")]',
        'type': 'xpath',
    }
    keypress_instructions_in_spanish = {
        'description': 'Instructions in Spanish for the Space game',
        'selector': '//span[contains(text(), "Aparecerá un temporizador de cuenta atrás.")]',
        'type': 'xpath',
    }
    keypress_game_space_bar = {
        'description': 'Space bar in Spanish',
        'selector': '//span[contains(text(), "barra espaciadora")]',
        'type': 'xpath',
    }
    balloons_instructions_in_spanish = {
        'description': 'Instructions in Spanish for Balloons game',
        'selector': '//span[contains(text(), "El objetivo de este juego es acumular la mayor cantidad de ")]',
        'type': 'xpath',
    }
    left_hand = {
        'description': 'Left hand in Spanish',
        'selector': '//span[contains(text(), "Izquierda")]',
        'type': 'xpath',
    }
    another_euro_symbol = {
        'description': 'Another selector for Euro symbol',
        'selector': '.icon-type__money-eur',
    }
    begin_in_spanish = {
        'description': 'Begin button in Spanish',
        'selector': '//span[(text() = "Iniciar")]',
        'type': 'xpath',
    }
    play_games_buttons = {
        'description': 'Play games 12 buttons',
        'selector': '//a[contains(text(), "Jugar")]',
        'type': 'xpath',
    }
    euro_symbol = {
        'description': 'Euro symbol',
        'selector': '//span[contains(text(), "€")]',
        'type': 'xpath',
    }
    euros_amount = {
        'description': 'Amount of money',
        'selector': '//span[contains(text(), "10")]',
        'type': 'xpath',
    }

    game1_title = {
        'description': 'Game 1 title in Spanish',
        'selector': '//span[contains(text(), "¡Enhorabuena!")]',
        'type': 'xpath',
    }
    balloons_pump = {
        'description': 'Balloons game pump in Spanish',
        'selector': '//span[contains(text(), "Hinchar")]',
        'type': 'xpath',
    }
    money_exchange2_instructions_in_spanish = {
        'description': 'Instructions in Spanish for Money exchange 2',
        'selector': '//span[contains(text(), "Para esta prueba, trabajarás con otro participante aleatorio. '
                    'Sigue las instrucciones que recibirás a lo largo de la prueba.")]',
        'type': 'xpath',
    }
    money_exchange2_text = {
        'description': 'Money exchange 2 some text',
        'selector': '//span[contains(text(), "Acabas de ganar")]',
        'type': 'xpath',
    }
    digits_game_instructions_in_spanish = {
        'description': 'Instructions in Spanish for Digits game',
        'selector': '//span[contains(text(), "Aparecerá rápidamente una secuencia de números de uno en uno.")]',
        'type': 'xpath',
    }
    digits_game_text = {
        'description': 'Digits game some text',
        'selector': '//span[contains(text(), "Introduce los dígitos que has visto y pulsa Intro.")]',
        'type': 'xpath',
    }
    easy_or_hard_instructions_in_spanish = {
        'description': 'Instructions in Spanish for game Easy or hard',
        'selector': '//span[contains(text(), "En cada prueba, podrás elegir entre dos tareas. ")]',
        'type': 'xpath',
    }
    easy_or_hard_text = {
        'description': 'Easy or hard some text',
        'selector': '//span[contains(text(), "Elige tu tarea")]',
        'type': 'xpath',
    }
    stop_instructions_in_spanish = {
        'description': 'Instructions in Spanish for Stop game',
        'selector': '//span[contains(text(), "barra espaciadora")]',
        'type': 'xpath',
    }
    cards_instructions_in_spanish = {
        'description': 'Instructions in Spanish for the Cards game',
        'selector': '//span[contains(text(), "El objetivo de este juego es ganar el máximo dinero posible mediante ")]',
        'type': 'xpath',
    }
    cards_text = {
        'description': 'Cards game some text',
        'selector': '//span[contains(text(), "Ganancias")]',
        'type': 'xpath',
    }
    arrows_instructions_in_spanish = {
        'description': 'Instructions in Spanish for the Arrows game',
        'selector': '//span[contains(text(), "Si las flechas son de color ")]',
        'type': 'xpath',
    }
    length_instructions_in_spanish = {
        'description': 'Instructions in Spanish for the Length game',
        'selector': '//span[contains(text(), "Verás una de las dos caras: ")]',
        'type': 'xpath',
    }
    towers_instructions_in_spanish = {
        'description': 'Instructions in Spanish for the Towers game',
        'selector': '//span[contains(text(), "Deshacer movimiento")]',
        'type': 'xpath',
    }
    towers_text = {
        'description': 'Towers game some text',
        'selector': '//span[contains(text(), "Borrar todo")]',
        'type': 'xpath',
    }
    faces_game_instructions_in_spanish = {
        'description': 'Instructions in Spanish for Faces game',
        'selector': '//span[contains(text(), "Te mostraremos fotografías de personas con diferentes expresiones ")]',
        'type': 'xpath',
    }
    faces_game_text = {
        'description': 'Some text at Faces game',
        'selector': '//div[contains(text(), "Disgusto")]',
        'type': 'xpath',
    }
    intro_text = {
        'description': 'Spanish text in intro page for the interview',
        'selector': '//h2[contains(text(), "Te damos la bienvenida a la entrevista de pymetrics.")]',
        'type': 'xpath',
    }
    introduction_title_in_spanish = {
        'description': 'Intro title for the interview',
        'selector': '//a[(text() = "Introducción")]',
        'type': 'xpath',
    }
    about_company_in_spanish = {
        'description': 'About company title for the interview',
        'selector': '//a[(text() = "Empresa")]',
        'type': 'xpath',
    }
    about_company_text_in_spanish = {
        'description': 'About company text for the interview',
        'selector': '//h1[(text() = "Acerca de esta función")]',
        'type': 'xpath',
    }
    min_spanish = {
        'description': 'About company text for the interview',
        'selector': '//div[(text() = "3 minutos")]',
        'type': 'xpath',
    }
    what_to_expect = {
        'description': 'What to expect title in Spanish',
        'selector': '//a[(text() = "Qué esperar")]',
        'type': 'xpath',
    }
    emphasis_text = {
        'description': 'Emphasis text in Spanish',
        'selector': '//span[(text() = "la segunda grabación se enviará automáticamente")]',
        'type': 'xpath',
    }
    setup_text = {
        'description': 'Setup text in Spanish',
        'selector': '//h2[(text() = "Pruebas de configuración técnica")]',
        'type': 'xpath',
    }
    config_text = {
        'description': 'Config text in Spanish',
        'selector': '//h4[(text() = "Acerca de esta prueba")]',
        'type': 'xpath',
    }
    continue_in_spanish_interview = {
        'description': 'Continue button in Spanish',
        'selector': '//button[(text() = "Continuar")]',
        'type': 'xpath',
    }
    start_tests_interview = {
        'description': 'Start tests button in Spanish',
        'selector': '//button[(text() = "Comenzar pruebas")]',
        'type': 'xpath',
    }
    select_dropdown_interview = {
        'description': 'Select languages dropdown for the interview',
        'selector': 'select',
    }
    spanish_option_interview = {
        'description': 'Spanish language for the interview',
        'selector': '//option[(text() = "Español")]',
        'type': 'xpath',
    }
    configuration_popup = {
        'description': 'Language configuration pop up in Spanish',
        'selector': '//div[(text() = "Configuración de idioma")]',
        'type': 'xpath',
    }

    def getting_to_games(driver):
        LoginPage.login_spanish_user(driver, '/applications/341373/games/games-advice/')
        driver.wait_until_element_visible(RegisterPage.language_dropdown)
        driver.click(RegisterPage.language_dropdown)
        driver.click(RegisterPage.spanish_language_option)
        driver.click(Spanish.submit_language)
        driver.wait_until_element_visible(Spanish.game_advice_spanish)
        driver.click(Spanish.submit_game_advice)
        driver.click(GamesPage.close_icon)
