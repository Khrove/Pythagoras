class StudentHomePage:
    def __init__(self, page):
        self.page = page
        self.assessment_title = page.locator('.card--assessments__title h2')
        self.right_btn = page.locator('[data-testid="next-arrow"]')

    def wait_for_page(self):
        self.page.wait_for_load_state('networkidle')

    def open_assessment(self, assessment: str):
        amount = self.assessment_title.count()
        for i in range(amount):
            title = self.assessment_title.nth(i).text_content()
            if title != assessment:
                self.scroll_assessment()
            if title == assessment:
                self.assessment_title.nth(i).click()

    def scroll_assessment(self):
        self.right_btn.click()
