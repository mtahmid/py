from tests.ui_tests.pages.base_page import BasePage


class Admin(BasePage):
    admin_button = {
        'description': 'Admin button',
        'selector': '[title="Administration"]',
    }
    user_row_title = {
        'description': 'User row title',
        'selector': '//p[contains(text(), "User")]',
        'type': 'xpath',
    }
    interviews_settings = {
        'description': 'Interviews Settings',
        'selector': '//a[contains(text(), "Interviews")]',
        'type': 'xpath',
    }
    questions_tab = {
        'description': 'Questions tab under interview setup',
        'selector': "//a[contains(@href,'questions')]",
        'type': 'xpath',
    }
    add_interview_button = {
        'description': 'Add Interview button',
        'selector': '//button[contains(text(), "Add Interview")]',
        'type': 'xpath',
    }
    styles_and_branding_settings = {
        'description': 'Styles & Branding Settings',
        'selector': '//a[contains(text(), "Styles & Branding")]',
        'type': 'xpath',
    }
    type_question = {
        'description': 'Type a question input field',
        'selector': '[placeholder="Type Question Text"]',
    }
    duplicate_icon = {
        'description': 'Duplicate interview icon',
        'selector': '[data-for="duplicateInterviewIcon"]',
    }
    select_placeholder = {
        'description': 'Select placeholder under duplicate interview',
        'selector': '.Select-placeholder',
    }
    position_ten = {
        'description': 'Additional position 10',
        'selector': '[aria-label="Additional position 10"]',
    }
    duplicate_button = {
        'description': 'Duplicate button',
        'selector': '//span[text()="Duplicate"]',
        'type': 'xpath',
    }
    add_question = {
        'description': 'Add question button',
        'selector': '//span[text()="Add Question"]',
        'type': 'xpath',
    }
    automated_question = {
        'description': 'New question created',
        'selector': "//textarea[text()='Automated question']",
        'type': 'xpath',
    }
    remove_interview = {
        'description': 'Remove interview icon',
        'selector': "//i[@class='fa fa-trash-o']",
        'type': 'xpath',
    }
    dev_report_toggle = {
        'description': 'Development report toggle',
        'selector': '.react-switch-handle',
    }
    toggle_text = {
        'description': 'The text under the toggle',
        'selector': '._2IQNomcSEx1Q1nacKWoJdt',
    }
    save_button = {
        'description': 'Save button',
        'selector': '//button[contains(text(), "Save")]',
        'type': 'xpath',
    }
    leadership_subtab = {
        'description': 'Save button',
        'selector': '//a[contains(text(), "Leadership")]',
        'type': 'xpath',
    }
    check_mark = {
        'description': 'Check mark after saving',
        'selector': '.fa.fa-check',
    }
    create_position_template = {
        'description': 'Create a template button',
        'selector': '//button[contains(text(), "Create Position")]',
        'type': 'xpath',
    }
    templates = {
        'description': 'Different position templates',
        'selector': '._1BzSrRdwgm6DENNYHnkoWY._3dK6MPB66K3zBeaZbdrIyQ',
    }
    position_name = {
        'description': 'Position name input field',
        'selector': '#position_template_configuration_title',
    }
    archive_template = {
        'description': 'Archive the template button',
        'selector': '[alt="archive position template"]',
    }
    warning = {
        'description': 'Warning message',
        'selector': '.fa.fa-warning',
    }
    continue_button = {
        'description': 'Continue button',
        'selector': '//button[contains(text(), "Continue")]',
        'type': 'xpath',
    }
    manager_flag = {
        'description': 'Manager toggle under Insights tab in Admin',
        'selector': '//div[text() = "Manager"]',
        'type': 'xpath',
    }
    switches = {
        'description': 'Different toggles under Admin page',
        'selector': '.react-switch',
    }
    login_preview_button = {
        'description': 'Login Preview Button',
        'selector': '//button[contains(text(), "Login Preview")]',
        'type': 'xpath',
    }

    def interview_toggle(self, index):
        toggle = {
            'description': f'Interview toggle {index}',
            'selector': f'(//div[@class="react-switch-bg"])[{index}]',
            'type': 'xpath',
        }
        return toggle

# flake8: noqa
