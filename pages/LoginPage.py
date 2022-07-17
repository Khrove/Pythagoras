import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.loginWithEmailBtn = page.locator('button[class*="LoginWithEmailOption"]')
        self.emailInput = page.locator('#email')
        self.passwordInput = page.locator('#password')
        self.loginBtn = page.locator('[aria-label="Log in"]')

    def navigate(self):
        self.page.goto(os.environ.get("UAT_URL"))

    def login(self, username, password):
        self.loginWithEmailBtn.click()
        self.emailInput.fill(username)
        self.passwordInput.fill(password)
        self.loginBtn.click()
