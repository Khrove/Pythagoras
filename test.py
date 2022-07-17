import globals
import os
from os.path import join, dirname
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from pages.LoginPage import LoginPage
from pages.explore.GradeView import ExploreGradeView
from pages.explore.ModuleView import ExploreModuleView
from pages.assess.Assess import AssessPage

load_dotenv()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def main():
    with sync_playwright() as p:
        globals.init()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        grade_view = ExploreGradeView(page)
        module_view = ExploreModuleView(page)
        assess_page = AssessPage(page)

        login_page.navigate()
        login_page.login(os.environ.get("T1_REG1"), os.environ.get("PASSWORD"))
        grade_view.validate_level('Level 3')
        grade_view.validate_module_title('Units of Any Number')
        grade_view.click_on_module('Multiplication and Area')
        module_view.validate_title('Multiplication and Area')
        module_view.select_assessment('Module 4 Assessment version 1')

        assess_page.validate_title('Level 3, Module 4, Module Assessment 1')
        assess_page.assign_assessment('Class 2022-23')

        browser.close()


if __name__ == '__main__':
    main()
