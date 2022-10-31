from tests.ui_tests.pages.base_page import BasePage


class Prospects(BasePage):
    prospects_button = {
        'description': 'Prospects tab',
        'selector': '[title="Prospects"]',
    }
    empty = {
        'description': 'Text for empty page',
        'selector': "//h3[contains(text(), 'Sorry')]",
        'type': 'xpath',
    }
    current_location = {
        'description': 'Current location column header',
        'selector': "//*[text()='Current Location']",
        'type': 'xpath',
    }
    number_of_pages = {
        'description': 'Number of pages on the bottom of the page',
        'selector': '._13gCJ0VEonEQvBQWyc7-YI ',
    }
    prospects_list = {
        'description': 'Incumbents list',
        'selector': '._2lo4cYsONgZjlD_BFbmvCr > div',
    }
    prospect_email = {
        'description': 'Prospect email inside the card',
        'selector': '#noun_Mail_3370539',
    }
    prospect_resume = {
        'description': 'Prospect resume inside the card',
        'selector': '[data-for="resume-download"]',
    }
    prospect_linkedin = {
        'description': 'Prospect linkedin inside the card',
        'selector': '[data-for="linkedIn-link"]',
    }
    fit_details = {
        'description': 'Fit details under the card',
        'selector': "//*[text()='FIT DETAILS']",
        'type': 'xpath',
    }
    skills_breakdown = {
        'description': 'Skills breakdown under the card',
        'selector': "//*[text()='SKILLS BREAKDOWN']",
        'type': 'xpath',
    }
    prospects_filter = {
        'description': 'Filters button under prospects tab',
        'selector': "//*[text()='Filters']",
        'type': 'xpath',
    }
    positions = {
        'description': 'Different positions at Prospects tab',
        'selector': '._3gYaZnYddYWFjq3tJcUItz:first-child > div [data-for]',
    }
    positions_check = {
        'description': 'Checkboxes of different positions at Interviews',
        'selector': '._3gYaZnYddYWFjq3tJcUItz:first-child > div [type]',
    }
    search_city = {
        'description': 'Input field to search for the city under Filters',
        'selector': '[placeholder="Search city..."]',
    }
    ny_city_location = {
        'description': 'NY city option under location',
        'selector': '//span[text()="New York City, NY"]',
        'type': 'xpath',
    }
    position_location = {
        'description': 'Location underProspects card',
        'selector': '._1HgmpALIbnSnwbr2YbsMe4',
    }
