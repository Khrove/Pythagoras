from components.globals.hamburger import HamburgerComp


class HeaderComp:
    def __init__(self, page, root):
        context = page.locator(root)
        self.hamburger_comp = HamburgerComp(page, '#hamburger-menu-id-controls')
