from playwright.sync_api import sync_playwright
from pages.LoginPage import LoginPage
from pages.explore.GradeView import ExploreGradeView


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        grade_view = ExploreGradeView(page)

        login_page.navigate()
        login_page.login('sit_t1_reg1auto@yopmail.com', 'Test@123')
        grade_view.validate_module_title('Units of Any Number')
        grade_view.click_on_module('Multiplication and Area')

        browser.close()


if __name__ == '__main__':
    main()
