from playwright.sync_api import expect
import globals


class AssessPage:
    def __init__(self, page):
        globals.init()
        self.title = page.locator('.title')

    def validate_title(self, title):
        expect(self.title).to_have_text(title, timeout=globals.timeout)

