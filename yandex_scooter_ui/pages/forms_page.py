import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FormsPage(BasePage):
    TOP_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    BOTTOM_BUTTON = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")
    FURTHER =  (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Далее']")
    FIRST_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_CHOICE = (By.XPATH, ".//div[@class='select-search__select'][@value='Красногвардейская']")
    USER_NUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    DELIVERY_TIME = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_INPUT = (By.XPATH, ".//div[@class='Dropdown-placeholder is-selected']")
    RENTAL_PERIOD_CHOICE = (By.XPATH, ".//div[@class='Dropdown-option'][text()='семеро суток']")
    COLOR_CHOICE = (By.XPATH, ".//input[@id='black'][@class='Checkbox_Input__14A2w']")
    COMMENTS = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    MAKE_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Заказать']")
    CONFIRM_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Да']")
    STATUS_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Посмотреть статус']")
    #//div[@class='...']//input[@value='...'],//div[@class='select-search__select']//input[@value='Красногвардейская']


    @allure.step("Проверка перехода через верхнюю кнопку заказать")
    def go_to_order_forms_through_top_button(self):
        self.click(FormsPage.TOP_BUTTON)

    @allure.step("Проверка перехода через нижнюю кнопку заказать")
    def go_to_order_forms_through_bottom_button(self):
        self.scroll_to_element(FormsPage.BOTTOM_BUTTON)
        self.click(FormsPage.BOTTOM_BUTTON)

    @allure.step("Заполнение формы имени {first_name}")
    def fill_up_first_name_field(self, first_name):
        self.fill_up_text_field(FormsPage.FIRST_NAME, first_name)

    @allure.step("Заполнение формы фамилии {last_name}")
    def fill_up_last_name_field(self, last_name):
        self.fill_up_text_field(FormsPage.LAST_NAME, last_name)

    @allure.step("Заполнение формы эмейла {adress}")
    def fill_up_user_adress_field(self, adress):
        self.fill_up_text_field(FormsPage.ADRESS, adress)

    @allure.step("Выбор станции метро {metro}")
    def choice_metro_station(self, metro):
        
        
        self.wait_visibility_of_element_located(FormsPage.METRO_CHOICE)
        self.scroll_to_element(FormsPage.METRO_CHOICE)
        self.wait_visibility_of_element_located(FormsPage.METRO_CHOICE)
        self.click(FormsPage.METRO_CHOICE)
        
    @allure.step("Заполнение формы телефона {user_number}")
    def fill_up_user_number_field(self, user_number):
        self.fill_up_text_field(FormsPage.USER_NUMBER, user_number)

    @allure.step("Заполнение формы с данными первого раздела {data_form}")
    def fill_up_text_box_first_form(self, data_form):
        self.fill_up_first_name_field(data_form.get('first_name'))
        self.fill_up_last_name_field(data_form.get('last_name'))
        self.fill_up_user_adress_field(data_form.get('address'))
        self.choice_metro_station(data_form.get('metro'))
        self.fill_up_user_number_field(data_form.get('user_number'))

    @allure.step("Перейти к следующему разделу заполнения формы")
    def go_to_next_section(self):
        self.click(FormsPage.FURTHER)

    @allure.step("Заполнение формы когда доставят самокат {delivery_time}")
    def fill_up_delivery_time_field(self, delivery_time):
        self.fill_up_text_field(FormsPage.DELIVERY_TIME, delivery_time)

    @allure.step("Выбор срока аренды")
    def fill_up_rental_period_field(self):
        self.click(FormsPage.RENTAL_PERIOD_INPUT)
        self.fill_up_text_field(FormsPage.RENTAL_PERIOD_CHOICE)
        self.click(FormsPage.RENTAL_PERIOD_CHOICE)

    @allure.step("Выбор цвета самоката")
    def fill_up_color_choice_field(self):
        self.click(FormsPage.RENTAL_PERIOD_INPUT)
        self.fill_up_text_field(FormsPage.RENTAL_PERIOD_CHOICE)
        self.click(FormsPage.RENTAL_PERIOD_CHOICE)

    @allure.step("Заполнение формы коментария {comments}")
    def fill_up_comments_field(self, comments):
        self.fill_up_text_field(FormsPage.COMMENTS, comments)

    @allure.step("Заполнение формы с данными последнего раздела {data_form}")
    def fill_up_text_box_last_form(self, data_form):
        self.fill_up_delivery_time_field(data_form.get('delivery_time'))
        self.fill_up_comments_field(data_form.get('comments'))

    @allure.step("Подтверждение формы заказа")
    def confirm_of_order_form(self):
        self.click(FormsPage.MAKE_ORDER)
        self.click(FormsPage.CONFIRM_ORDER)

    @allure.step("Просмотр статуса заказов")
    def view_order_status(self):
        self.click(FormsPage.STATUS_ORDER)
    