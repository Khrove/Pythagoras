class StudentAssessmentPage:
    def __init__(self, page):
        self.page = page
        self.start_btn = page.locator('[aria-label="Start assessment"]')
        self.questions = page.locator('.lrn-assess-item')
        self.next_btn = page.locator('.bottom-right-wrapper #lrn_assess_next_btn')

    def wait_for_page(self):
        self.page.wait_for_load_state('networkidle')

    def start_assessment(self):
        self.start_btn.click()

    def click_next_btn(self):
        self.next_btn.click()

    def complete_radio_question(self, question, part, answer):
        self.questions.nth(question).locator('[type="radio"], .lrn-mcq-option').nth(answer).click()

    def complete_input_question(self, question, part, answer):
        self.questions.nth(question).locator('.lrn_textinput').nth(part).click()
        self.questions.nth(question).locator('.lrn_textinput').nth(part).type(answer)

    def complete_box_click_question(self, question, answer):
        self.questions.nth(question).locator('.lrn-shading-cell').nth(answer).click()
