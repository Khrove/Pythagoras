from playwright.sync_api import expect
from components.modals.assignEntity import AssignEntityModal
import globals


class AssessPage:
    def __init__(self, page):
        globals.init()
        self.title = page.locator('.title')
        self.assign_btn = page.locator('[data-dp-analytics-id="AssignAssessment"]')
        self.assign_modal = AssignEntityModal(page, '#assign-modal-content')

    def validate_title(self, title):
        expect(self.title).to_have_text(title, timeout=globals.timeout)

    def assign_assessment(self, classname):
        self.assign_btn.click()
        self.assign_modal.assign_class(classname)
        self.assign_modal.assign_btn.click()
