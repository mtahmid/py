from tests.ui_tests.pages.base_page import BasePage


class MarketplacePage(BasePage):
    join_the_marketplace_btn = {
        'description': 'Join the Marketplace button',
        'selector': '.btn.block.m-b.watermelon-background',
    }
    disabled_submit_btn = {
        'description': 'Disabled submit button',
        'selector': '.submit-input-button.disabled',
    }
    client_matches_list = {
        'description': 'Client matches list',
        'selector': '.client-matches-list',
    }
    client_matches_close_btn = {
        'description': 'Client matches list close button',
        'selector': '.blue-chill-background',
    }
    matches_card_list = {
        'description': 'Matches card list',
        'selector': '.matches-card-list',
    }
    matches_nav = {
        'description': 'Top Matches nav',
        'selector': '#matches-nav',
    }
    matches_header = {
        'description': 'Matches header',
        'selector': 'h1.regular-font.ng-binding',
    }
    pymetrics_logo = {
        'description': 'Pymetrics logo',
        'selector': '.self-center.logo',
    }
    error_message = {
        'description': 'Ineligible error message',
        'selector': '//h4[contains(text(), "Sorry")]',
        'type': 'xpath',
    }
    please_contact_msg = {
        'description': 'Please contact support message',
        'selector': '//h4[contains(text(), "Please contact")]',
        'type': 'xpath',
    }
    error_message_home_btn = {
        'description': 'Home button on error message',
        'selector': '[ng-click="navigateToRoot()"]',
    }
    education_dropdown = {
        'description': 'Education dropdown',
        'selector': '#highest_ed',
    }
    high_school_option = {
        'description': 'High school option in the education dropdown',
        'selector': '//option[contains(text(), "High school")]',
        'type': 'xpath',
    }
    graduation_year_dropdown = {
        'description': 'Graduation year dropdown',
        'selector': '#grad-year',
    }
    graduation_year_2002_option = {
        'description': 'High school option in the graduation year dropdown',
        'selector': '//option[contains(text(), "2002")]',
        'type': 'xpath',
    }
    current_location_textbox = {
        'description': 'Current location textbox',
        'selector': '[placeholder="Current Location"]',
    }
    realtime_city_matches = {
        'description': 'City match dropdown',
        'selector': '.uib-typeahead-match',
    }
    active_realtime_city_match = {
        'description': 'Active realtime city match',
        'selector': '.uib-typeahead-match.active',
    }
    submit_button = {
        'description': 'Submit button',
        'selector': '.submit-button',
    }
    match_loading_page = {
        'description': 'Match loading page',
        'selector': '.matches-page',
    }
    match_loading_page_close_btn = {
        'description': 'Match loading page close button',
        'selector': '[ng-click="stopTimeout()"]',
    }
    no_marketplace_match_image = {
        'description': 'No marketplace match image',
        'selector': '[src="/static/internal/matches/img/no-mktp-matches.png"]',
    }
    no_marketplace_match_text = {
        'description': 'No marketplace match text',
        'selector': '//h5[contains(text(), "working with a great")]',
        'type': 'xpath',
    }
    filter_section = {
        'description': 'Filter section',
        'selector': '#filter-selection',
    }
    no_matches_loading_overlay = {
        'description': 'Loading indicator for no matches',
        'selector': '[ng-if="!matches || loading"]',
    }
    complete_action_items_header = {
        'description': 'Complete action items header',
        'selector': '.grey-header',
    }
    careers = {
        'description': 'Different careers',
        'selector': '[career] .banner-container',
    }
    recommended_jobs = {
        'description': 'Recommended jobs tab',
        'selector': '#recommended-jobs-nav',
    }
    complete_action_text = {
        'description': 'Complete action item text',
        'selector': '//a[contains(text(), "completing")]',
        'type': 'xpath',
    }
    complete_games = {
        'description': 'Common app',
        'selector': '[role="button"]',
    }
    partner_roles = {
        'description': 'See all partner roles',
        'selector': '.partner-roles-link.ng-binding',
    }
    multiple_locations = {
        'description': 'Multiple locations card',
        'selector': '//div[text()[normalize-space() = "Multiple locations"]]',
        'type': 'xpath',
    }
    filter_dropdown = {
        'description': 'Matches filter drop down',
        'selector': '//span[contains(text(), "Match Type")]',
        'type': 'xpath',
    }
    filter_checkboxes = {
        'description': 'Filter checkboxes',
        'selector': '[type="checkbox"]',
    }
    apply_button = {
        'description': 'Apply button',
        'selector': '//button[contains(text(), "Apply")]',
        'type': 'xpath',
    }
    careers_number = {
        'description': 'Number of filtered careers',
        'selector': '#filter-count .watermelon',
    }
    clear_filter = {
        'description': 'Clear filters button',
        'selector': '.clear-filter',
    }
    clear_all_filters = {
        'description': 'Clear filters button under partners tab',
        'selector': '[name="clearMarketplaceFilter"]',
    }
    ineligible = {
        'description': 'No eligible message',
        'selector': 'h3',
    }
    see_more_courses = {
        'description': 'See more courses button',
        'selector': '//div[contains(text(), "See more courses")]',
        'type': 'xpath',
    }
    skills = {
        'description': 'Skills under careers tab',
        'selector': '.skill',
    }
    open_jobs = {
        'description': 'Open jobs subtab',
        'selector': '[ui-sref=".jobs"]',
    }
    courses = {
        'description': 'Courses subtab',
        'selector': '[ui-sref=".courses"]',
    }
    jobs = {
        'description': 'Different jobs',
        'selector': '[job="job"]',
    }
    different_courses = {
        'description': 'Different courses under Courses tab',
        'selector': '[course="course"]',
    }
