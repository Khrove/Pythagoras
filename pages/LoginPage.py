class LoginPage:
    def __init__(self, page):
        self.page = page
        self.loginWithEmailBtn = page.locator('button[class*="LoginWithEmailOption"]')
        self.emailInput = page.locator('#email')
        self.passwordInput = page.locator('#password')
        self.loginBtn = page.locator('[aria-label="Log in"]')

    def navigate(self):
        self.page.goto("https://digital.uat.greatminds.dev")

    def login(self, username, password):
        self.loginWithEmailBtn.click()
        self.emailInput.fill(username)
        self.passwordInput.fill(password)
        self.loginBtn.click()
