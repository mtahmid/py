from tests.ui_tests.pages.base_page import BasePage


class CandidateInviteSingle(BasePage):
    position_dropdown = {
        'description': 'Position dropdown',
        'selector': '.Select.positionSelect',
    }
    active_position = {
        'description': 'Active position',
        'selector': '//div[contains(@role,"option") and .//text()="Test ACT Position (USA, SC)"]', # noqa
        'type': 'xpath',
    }
    first_name_textbox = {
        'description': 'First Name Textbox',
        'selector': '[name="firstName"]',
    }
    last_name_textbox = {
        'description': 'Last Name Textbox',
        'selector': '[name="lastName"]',
    }
    email_name_textbox = {
        'description': 'Email Textbox',
        'selector': '[name="email"]',
    }
    submit = {
        'description': 'Submit button',
        'selector': '#invite-single-candidate-submit-button',
    }
    bcc_email = {
        'description': 'Email in Bcc section',
        'selector': '._1tc0RRTTMSO543GLHezXlS',
    }
    send_from_placeholder_name = {
        'description': 'Send from placeholder name',
        'selector': '[placeholder="Py Metrics"]',
    }
    reply_to_placeholder = {
        'description': 'Reply To placeholder',
        'selector': '[placeholder="Email"]',
    }
    email_subject = {
        'description': 'Email subject',
        'selector': '[placeholder="Email Subject"]',
    }
    variables_available = {
        'description': 'Variables available',
        'selector': '._2bqEJ2-rUhMFFUmtFm7-BQ',
    }
    exit = {
        'description': 'Exit button',
        'selector': '._1ZmrjvbfLr11RZ2yEJ1vIJ button',
    }
    logout = {
        'description': 'Log out button',
        'selector': '[title="Log Out"]',
    }
    login_form = {
        'description': 'Log in form under registration',
        'selector': '#login-form',
    }
    whitelist = {
        'description': 'Whitelist button',
        'selector': '#candidates-whitelist-button',
    }
