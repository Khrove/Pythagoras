

class AssignPage:
    def __init__(self, page):
        self.page = page
        self.assignment_record_comp = page.locator('[data-testid="card-list-item"]')
        self.delete_btn = page.locator('div[class*="WarningDeleteModal"] button:nth-child(2)')

    def wait_for_page(self):
        self.page.wait_for_load_state(state='networkidle')

    def get_assignment_record(self, record: str):
        self.assignment_record_comp.locator(":scope", has_text=f"{record}").locator('.right-card button[id*="assessment-card-button"]').first.click()

    def delete_assignment(self, record: str):
        is_found = self.assignment_record_comp.locator(":scope", has_text=f"{record}").first.is_visible()
        if is_found:
            self.assignment_record_comp.locator(":scope", has_text=f"{record}").locator('.right-card [aria-label="Additional options"]').first.click()
            self.assignment_record_comp.locator(":scope", has_text=f"{record}").locator(
                    '.right-card #Delete').click()
            self.delete_btn.click()
