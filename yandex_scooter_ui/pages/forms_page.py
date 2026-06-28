import allure
import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FormsPage(BasePage):
    ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    FURTHER =  (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Далее']")
    FIRST_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, 'select-search__input')
    METRO_CHOICE = (By.CLASS_NAME, 'select-search__select')
    USER_NUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    DELIVERY_TIME = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_INPUT = (By.XPATH, ".//div[@class='Dropdown-placeholder is-selected']")
    RENTAL_PERIOD_CHOICE = (By.XPATH, ".//div[@class='Dropdown-option'][text()='семеро суток']")
    COLOR_CHOICE = (By.XPATH, ".//input[@id='black'][@class='Checkbox_Input__14A2w']")
    COMMENTS = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    MAKE_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Заказать']")
    CONFIRM_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Да']")
    STATUS_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Посмотреть статус']")
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')


    @allure.step('Принятие cookies')
    def accept_cookie(self):
        self.click(self.COOKIE_BUTTON)

    @allure.step('Переход к заказу')
    def go_to_order_button(self):
        self.click(FormsPage.ORDER_BUTTON)

    @allure.step('Перейти далее')
    def go_to_further_button(self):
        self.click(FormsPage.FURTHER)

    @allure.step("Заполнение первой формы заказа")
    def fill_first_form(
            self,
            first_name,
            last_name,
            address,
            metro,
            user_number
    ):

        self.send_keys(self.FIRST_NAME, first_name)
        time.sleep(3)
        self.send_keys(self.LAST_NAME, last_name)
        time.sleep(3)
        self.send_keys(self.ADDRESS, address)
        time.sleep(3)
        self.click(self.METRO_INPUT)
        time.sleep(3)
        self.send_keys(self.METRO_INPUT, metro)
        time.sleep(3)
        self.click(self.METRO_CHOICE)
        time.sleep(3)
        self.send_keys(self.USER_NUMBER, user_number)


    