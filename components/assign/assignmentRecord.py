import playwright.async_api


class AssignmentRecord:
    def __init__(self, page, context: str | playwright.async_api.Locator):
        self.page = page

