from tests.ui_tests.pages.base_page import BasePage


class VideoAssessmentWelcomePage(BasePage):
    pymetrics_logo = {
        'description': 'Pymetrics logo',
        'selector': '[src="/static/video/assessment/static'
        '/media/logo-icon.c2e09b76.png"]',
    }
    close_icon = {
        'description': 'Close icon',
        'selector': '.close-icon',
    }
    continue_button = {
        'description': 'Continue button',
        'selector': '.btn-pink',
    }
    title_header = {
        'description': 'Title header',
        'selector': '.title',
    }
    role_video = {
        'description': 'About This Role video',
        'selector': '#video-element',
    }
    expectation_page = {
        'description': 'What to expect page',
        'selector': '.expectation-page',
    }
    expectation_continue_button = {
        'description': 'Continue button on What To Expect page',
        'selector': '.btn-pink-block',
    }
    video_player_preview = {
        'description': 'Preview player in Set up Mode',
        'selector': '.player',
    }
    setup_mode_title = {
        'description': 'Set up Mode title',
        'selector': '.title',
    }
    test_progress_bar = {
        'description': 'Technical Setup Tests progress bar',
        'selector': '.bar-container',
    }
