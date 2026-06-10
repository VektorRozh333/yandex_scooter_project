import allure
import data

from pages.questions_page import QuestionsPage


class TestQuestionsPage:
    @allure.title("Проверка доступности страницы")
    def test_questions_is_avaliable(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.open(data.BASE_URL)

    @allure.title("При клике на первый вопрос должен появиться выпадающий список с ответом")
    def test_questions_click_on_first_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.open(data.BASE_URL)
        questions_page.click_on_first_question()

    @allure.title("При клике на второй вопрос должен появиться выпадающий список с ответом")
    def test_questions_click_on_second_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.open(data.BASE_URL)
        questions_page.click_on_second_question()

    @allure.title("При клике на третий вопрос должен появиться выпадающий список с ответом")
    def test_questions_click_on_third_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.open(data.BASE_URL)
        questions_page.click_on_third_question()
    
    @allure.title("При клике на четвёртый вопрос должен появиться выпадающий список с ответом")
    def test_questions_click_on_fourth_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.open(data.BASE_URL)
        questions_page.click_on_fourth_question()

    @allure.title("При клике на пятый вопрос должен появиться выпадающий список с ответом")
    def test_questions_click_on_fifth_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.open(data.BASE_URL)
        questions_page.click_on_fifth_question()

    @allure.title("При клике на шестой вопрос должен появиться выпадающий список с ответом")
    def test_questions_click_on_sixth_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.open(data.BASE_URL)
        questions_page.click_on_sixth_question()

    @allure.title("При клике на седьмой вопрос должен появиться выпадающий список с ответом")
    def test_questions_click_on_seventh_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.open(data.BASE_URL)
        questions_page.click_on_seventh_question()

    @allure.title("При клике на восьмой вопрос должен появиться выпадающий список с ответом")
    def test_questions_click_on_eighth_question(self, driver):
        questions_page = QuestionsPage(driver)
        questions_page.open(data.BASE_URL)
        questions_page.click_on_eighth_question()
