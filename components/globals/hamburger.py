class HamburgerComp:
    def __init__(self, page, root):
        self.page = page
        context = page.locator(root)
        self.hamburger_btn = page.locator('[aria-label*="hamburguer"]')
        self.option_container = context.locator('#drawer-content-hamburger-menu-id-controls')

    def click_hamburger_option(self, option):
        self.option_container.locator(f'[aria-label="{option}"] div').click()
