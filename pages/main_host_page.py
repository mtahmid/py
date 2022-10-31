import tests.ui_tests.utils.configs as configs

from tests.ui_tests.pages.base_page import BasePage


class MainPage(BasePage):
    loginTab = {
        'description': 'Login tab on homepage',
        'selector': '//a[@href="/login/"]',
        'type': 'xpath'
    }
    candidatesTab = {
        'description': 'Candidates tab on homepage',
        'selector': '.nav-link[href="/candidates"]',
    }
    solutionsTab = {
        'description': 'Solutions tab on homepage',
        'selector': '.nav-link[href="/solutions"]',
    }
    solutionsHeroBackground = {
        'description': 'Solutions hero background',
        'selector': '.solutions-hero-bg',
    }
    candidatesHeroBackground = {
        'description': 'Candidates hero background',
        'selector': '.candidates-hero-bg',
    }
