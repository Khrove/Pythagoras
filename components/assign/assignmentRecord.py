import playwright.async_api


class AssignmentRecord:
    def __init__(self, page, context):
        self.page = page
        self.context = context

    def click_action_btn(self, record):
        self.context.locator(f'text="{record}"').locator('.right-card button[id*="assessment-card-button"]').click()

