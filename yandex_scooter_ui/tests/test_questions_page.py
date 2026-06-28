import allure
import data
from pages.questions_page import QuestionsPage


class TestQuestionsPage:
    
    @allure.title("Проверка выпадающего списка в разделе вопроссы о важном")
    def test_questions(self, driver):
        questions_page = QuestionsPage(driver)

        with allure.step('Открытие главной страницы'):
            questions_page.open(data.BASE_URL)
        
        with allure.step('Принятие cookie'):
            questions_page.accept_cookie()

        with allure.step('прверка первого вопроса'):
            questions_page.click_on_first_question()
        
        with allure.step('прверка второго вопроса'):
            questions_page.click_on_second_question()

        with allure.step('прверка третьего вопроса'):
            questions_page.click_on_third_question()

        with allure.step('прверка четвёртого вопроса'):
            questions_page.click_on_fourth_question()

        with allure.step('прверка пятого вопроса'):
            questions_page.click_on_fifth_question()

        with allure.step('прверка шестого вопроса'):
            questions_page.click_on_sixth_question()

        with allure.step('прверка седьмого вопроса'):
            questions_page.click_on_seventh_question()

        with allure.step('прверка восьмого вопроса'):
            questions_page.click_on_eighth_question()

