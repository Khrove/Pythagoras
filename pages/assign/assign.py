from components.assign.assignmentRecord import AssignmentRecord


class AssignPage:
    def __init__(self, page):
        self.page = page
        self.assignment_record_comp = page.locator('[data-testid="card-list-item"]')

    def get_assignment_record(self, record: str):
        self.assignment_record_comp.locator(":scope", has_text=f"{record}").locator('.right-card button[id*="assessment-card-button"]').first.click()
