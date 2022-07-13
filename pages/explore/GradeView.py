from playwright.sync_api import expect


class ExploreGradeView:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('h3[class*="Title"]')
        self.moduleTitle = page.locator('div[class*="ModuleCard"] span')

    def validate_module_title(self, title):
        expect(self.title).to_have_text(title, timeout=10000)

    def click_on_module(self, title):
        self.page.locator(f'text={title}').click()
