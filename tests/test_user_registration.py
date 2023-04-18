from demoqa_tests.model.data.user import test_user
from demoqa_tests.model.pages.practice_form import PracticeForm
import allure


@allure.id("17096")
@allure.tag('Web')
@allure.title("test_registration_user")
def test_registration_user():
    with allure.step('Open practice form'):
        practice_form = PracticeForm(test_user)
    with allure.step('Submit form'):
        practice_form.submit_form()
    with allure.step('Validate form'):
        practice_form.should_have_submitted()
