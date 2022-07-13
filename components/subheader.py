class SubHeaderComp:
    def __init__(self, page):
        self.page = page
        self.curriculum_btn = page.locator('header > nav > ul > li:nth-child(1) > a')
