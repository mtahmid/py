from tests.ui_tests.pages.base_page import BasePage


class Faces(BasePage):
    pain_button = {
        'description': 'Pain button',
        'selector': '//*[contains(text(), "Pain")]',
        'type': 'xpath'
    }
    surprise_button = {
        'description': 'Pain button',
        'selector': '//*[contains(text(), "Surprise")]',
        'type': 'xpath'
    }
    happiness_button = {
        'description': 'Pain button',
        'selector': '//*[contains(text(), "Happiness")]',
        'type': 'xpath'
    }
    game_complete_text = {
        'description': 'Test Complete! message',
        'selector': '.game__title',
    }

    def complete_games(driver):
        driver.click(Faces.happiness_button)
        driver.click(Faces.pain_button)
        driver.click(Faces.surprise_button)
        driver.click(Faces.happiness_button)
        driver.click(Faces.pain_button)
        driver.click(Faces.surprise_button)
        driver.click(Faces.happiness_button)
        driver.click(Faces.pain_button)
        driver.click(Faces.surprise_button)
        driver.click(Faces.happiness_button)
        driver.click(Faces.pain_button)
        driver.click(Faces.surprise_button)
        driver.click(Faces.happiness_button)
        driver.click(Faces.pain_button)
