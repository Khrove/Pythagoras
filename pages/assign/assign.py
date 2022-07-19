from components.assign.assignmentRecord import AssignmentRecord

class AssignPage:
    def __init__(self, page):
        self.page = page

    def get_assignment_record(self, record: str):
        assignment_record_comp = AssignmentRecord(
            self.page,
            self.page.locator('', { has: page.locator(f'text="{record}"'} )))
