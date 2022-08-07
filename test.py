import globals
import os
from os.path import join, dirname
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from pages.LoginPage import LoginPage
from pages.explore.GradeView import ExploreGradeView
from pages.explore.ModuleView import ExploreModuleView
from pages.assess.Assess import AssessPage
from pages.assign.Assign import AssignPage
from pages.student.HomePage import StudentHomePage
from pages.student.assessment.Assessment import StudentAssessmentPage

load_dotenv()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def main():
    with sync_playwright() as p:
        globals.init()
        chromium = p.chromium
        browser = chromium.launch(headless=False)
        teacher_context = browser.new_context().new_page()
        student_context = browser.new_context().new_page()
        teacher_login_page = LoginPage(teacher_context)
        grade_view = ExploreGradeView(teacher_context)
        module_view = ExploreModuleView(teacher_context)
        assess_page = AssessPage(teacher_context)
        assign_page = AssignPage(teacher_context)

        student_login_page = LoginPage(student_context)
        student_home_page = StudentHomePage(student_context)
        student_assessment_page = StudentAssessmentPage(student_context)

        teacher_login_page.navigate()
        teacher_login_page.login(os.environ.get("T1_REG1"), os.environ.get("PASSWORD"))
        assess_page.navigate_to('Assign')
        assign_page.wait_for_page()
        assign_page.delete_assignment('Level 3, Module 4, Module Assessment 1')
        assess_page.navigate_to('Teach')

        grade_view.validate_level('Level 3')
        grade_view.validate_module_title('Units of Any Number')
        grade_view.click_on_module('Multiplication and Area')
        module_view.validate_title('Multiplication and Area')
        module_view.select_assessment('Module 4 Assessment version 1')

        assess_page.validate_title('Level 3, Module 4, Module Assessment 1')
        assess_page.assign_assessment('Class 2022-23')
        assess_page.navigate_to('Assign')

        assign_page.get_assignment_record('Level 3, Module 4, Module Assessment 1')

        student_login_page.navigate()
        student_login_page.login(os.environ.get("S1_REG1"), os.environ.get("PASSWORD"))
        student_home_page.wait_for_page()
        student_home_page.open_assessment('Level 3, Module 4, Module Assessment 1')

        student_assessment_page.start_assessment()
        student_assessment_page.complete_radio_question(0, 0, 1)
        student_assessment_page.complete_radio_question(0, 1, 0)
        student_assessment_page.complete_radio_question(0, 2, 1)
        student_assessment_page.click_next_btn()

        student_assessment_page.complete_input_question(1, 0, '2')
        student_assessment_page.click_next_btn()

        student_assessment_page.complete_radio_question(2, 0, 1)
        student_assessment_page.complete_box_click_question(2, 0)
        student_assessment_page.complete_box_click_question(2, 1)
        student_assessment_page.complete_select_question(2, 1, 1)
        student_assessment_page.click_next_btn()

        # assign_page.wait_for_page()
        # assign_page.delete_assignment('Level 3, Module 4, Module Assessment 1')

        browser.close()


if __name__ == '__main__':
    main()
