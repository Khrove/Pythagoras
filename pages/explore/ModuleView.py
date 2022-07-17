from playwright.sync_api import expect
from components.explore.moduleContainer import ModuleContainerComp
import globals


class ExploreModuleView:
    def __init__(self, page):
        self.page = page
        self.moduleContainerComp = ModuleContainerComp(page, 'section[class*="ModuleHeaderstyled__Wrapper"]')

    def validate_title(self, title):
        expect(self.moduleContainerComp.title).to_have_text(title, timeout=globals.timeout)

    def select_assessment(self, assessment):
        self.moduleContainerComp.assessments_dropdown.click()
        self.moduleContainerComp.get_assessment_option(assessment)
