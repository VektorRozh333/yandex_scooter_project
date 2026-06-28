import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class QuestionsPage(BasePage):
    
    FIRST_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-0']")
    SECOND_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-1']")
    THIRD_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-2']")
    FOURTH_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-3']")
    FIFTH_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-4']")
    SIXTH_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-5']")
    SEVENTH_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-6']")
    EIGHTH_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-7']")
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')


    @allure.step('Принятие cookies')
    def accept_cookie(self):
        self.click(self.COOKIE_BUTTON)


    @allure.step("Проверка кликабельности первого вопроса")
    def click_on_first_question(self):
        self.scroll_to_element(QuestionsPage.FIRST_QUESTION)
        self.click(QuestionsPage.FIRST_QUESTION)


    @allure.step("Проверка кликабельности второго вопроса")
    def click_on_second_question(self):
        self.scroll_to_element(QuestionsPage.SECOND_QUESTION)
        self.click(QuestionsPage.SECOND_QUESTION)


    @allure.step("Проверка кликабельности третьего вопроса")
    def click_on_third_question(self):
        self.scroll_to_element(QuestionsPage.THIRD_QUESTION)
        self.click(QuestionsPage.THIRD_QUESTION)


    @allure.step("Проверка кликабельности четвёртого вопроса")
    def click_on_fourth_question(self):
        self.scroll_to_element(QuestionsPage.FOURTH_QUESTION)
        self.click(QuestionsPage.FOURTH_QUESTION)


    @allure.step("Проверка кликабельности пятого вопроса")
    def click_on_fifth_question(self):
        self.scroll_to_element(QuestionsPage.FIFTH_QUESTION)
        self.click(QuestionsPage.FIFTH_QUESTION)


    @allure.step("Проверка кликабельности шестого вопроса")
    def click_on_sixth_question(self):
        self.scroll_to_element(QuestionsPage.SIXTH_QUESTION)
        self.click(QuestionsPage.SIXTH_QUESTION)


    @allure.step("Проверка кликабельности седьмого вопроса")
    def click_on_seventh_question(self):
        self.scroll_to_element(QuestionsPage.SEVENTH_QUESTION)
        self.click(QuestionsPage.SEVENTH_QUESTION)


    @allure.step("Проверка кликабельности восьмого вопроса")
    def click_on_eighth_question(self):
        self.scroll_to_element(QuestionsPage.EIGHTH_QUESTION)
        self.click(QuestionsPage.EIGHTH_QUESTION)
