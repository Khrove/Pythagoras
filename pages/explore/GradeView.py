from playwright.sync_api import expect
from components.subheader import SubHeaderComp


class ExploreGradeView:
    def __init__(self, page):
        self.page = page
        self.subheader = SubHeaderComp(page)
        self.title = page.locator('h3[class*="Title"]')
        self.moduleTitle = page.locator('div[class*="ModuleCard"] span')

    def validate_level(self, level):
        text = self.subheader.level_text.text_content()
        if text != level:
            self.subheader.level_btn.click()
            self.page.locator(f'text={level}').click()

    def validate_module_title(self, title):
        expect(self.title).to_have_text(title, timeout=10000)

    def click_on_module(self, title):
        self.page.locator(f'text={title}').click()
