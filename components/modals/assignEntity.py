
# Used in assigning assessments / assignments from teacher POV
class AssignEntityModal:
    def __init__(self, page, root):
        self.page = page
        self.context = page.locator(root)
        self.assign_btn = page.locator('[data-dp-analytics-id="AssignBasic"]')

    def assign_class(self, classname: str):
        self.context.locator(f'div[class*="classCheckbox"] div:has-text("{classname}") span').click()
