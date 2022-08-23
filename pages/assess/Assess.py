from playwright.sync_api import expect
from components.modals.assignEntity import AssignEntityModal
from components.globals.header import HeaderComp
import globals


class AssessPage:
    def __init__(self, page):
        globals.init()
        self.title = page.locator('.title')
        self.assign_btn = page.locator('[data-dp-analytics-id="AssignAssessment"]')
        self.assign_modal = AssignEntityModal(page, '#assign-modal-content')
        self.header_comp = HeaderComp(page, '[role="banner"]')
        self.start_time_open_btn = page.locator('#startDate .icon-chevron-up')
        self.launch_time_btn = page.locator('#TimePickerInput')
        self.time_option = page.locator('[data-testid="dropdown-option-text"]')

    def validate_title(self, title):
        expect(self.title).to_have_text(title, timeout=globals.timeout)

    def assign_assessment(self, classname):
        self.assign_btn.click()
        self.assign_modal.assign_class(classname)

    def update_start_time(self):
        self.start_time_open_btn.click()
        self.launch_time_btn.click()
        self.time_option.nth(3).click()

    def click_assign_btn(self):
        self.assign_btn.click()

    def navigate_to(self, app):
        self.header_comp.hamburger_comp.hamburger_btn.click()
        self.header_comp.hamburger_comp.click_hamburger_option(app)
