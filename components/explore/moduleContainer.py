

class ModuleContainerComp:
    def __init__(self, page, root):
        context = page.locator(root)
        self.title = context.locator('h2[class*="Title"]')
        self.assessments_dropdown = context.locator('div[class*="StyledAssessmentsAndQuiz"]')

    def get_assessment_option(self, assessment):
        self.assessments_dropdown.locator(f'[data-testid="dropdown-option-text"]:has-text("{assessment}")').click()
