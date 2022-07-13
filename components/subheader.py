class SubHeaderComp:
    def __init__(self, page):
        self.page = page
        self.curriculum_btn = page.locator('header > nav > ul > li:nth-child(1) > a')
        self.level_text = page.locator('[aria-controls="menu-courses"] span:nth-child(2) span')
        self.level_btn = page.locator('[aria-controls="menu-courses"]');