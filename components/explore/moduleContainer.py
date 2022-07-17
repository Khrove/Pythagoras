

class ModuleContainerComp:
    def __init__(self, page, root):
        context = page.locator(root)
        self.title = context.locator('h2[class*="Title"]')
