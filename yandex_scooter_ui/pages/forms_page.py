import allure
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
    RENTAL_PERIOD = (By.CLASS_NAME, 'Dropdown-placeholder')
    COLOR_BLACK = (By.ID, 'black')
    COLOR_GREY = (By.ID, 'grey')
    COMMENTS = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    MAKE_ORDER = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    CONFIRM_ORDER = (By.XPATH, ".//button[text()='Да']")
    STATUS_ORDER = (By.XPATH, ".//button[text()='Посмотреть статус']")
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


    @allure.step('Подтверждение заказа')
    def create_order(self):
        self.scroll_to_element(self.MAKE_ORDER)
        self.click(self.MAKE_ORDER)
        self.wait_clickable(self.CONFIRM_ORDER)
        self.click(self.CONFIRM_ORDER)
    

    @allure.step('Просмотр статуса заказа')
    def check_status_order(self):
        self.wait_clickable(self.STATUS_ORDER)
        self.click(self.STATUS_ORDER)


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
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.ADDRESS, address)

        self.click(self.METRO_INPUT)
        self.send_keys(self.METRO_INPUT, metro)
        self.click(self.METRO_CHOICE)

        self.send_keys(self.USER_NUMBER, user_number)


    @allure.step("Заполнение второй формы заказа")
    def fill_second_form(
            self,
            delivery_time,
            rental_period,
            color,
            comments
    ):
        
        self.click(self.DELIVERY_TIME)
        self.send_keys(self.DELIVERY_TIME, delivery_time)
        self.send_keys(self.DELIVERY_TIME, Keys.ENTER)

        self.click(self.RENTAL_PERIOD)
        rental_locator = (
            By.XPATH,
            f"(//div[@class='Dropdown-option'])[{rental_period}]"
        )
        self.click(rental_locator)

        if color == 'black':
            self.click(self.COLOR_BLACK)
        else:
            self.click(self.COLOR_GREY)

        self.send_keys(self.COMMENTS, comments)
