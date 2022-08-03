

class ModuleContainerComp:
    def __init__(self, page, root):
        self.page = page
        context = page.locator(root)
        self.title = context.locator('h2[class*="Title"]')
        self.assessments_dropdown = context.locator('[data-testid="navigation-menu-container"] button')

    def get_assessment_option(self, assessment):
        self.page.locator(f'[data-testid="navigation-menu-item"]:has-text("{assessment}")').click()
