import allure
import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogoPage(BasePage):

    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать']")
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')


    @allure.step('Принятие cookies')
    def accept_cookie(self):
        self.click(self.COOKIE_BUTTON)


    @allure.step('Нажатие верхней кнопки Заказать')
    def click_on_order_logo(self):
        self.click(self.ORDER_BUTTON)


    @allure.step("Проверка перехода на главную страницу Самоката")
    def click_on_scooter_logo(self):
        self.click(LogoPage.SCOOTER_LOGO)


    @allure.step("Проверка кликабельности логотипа Яндекса")
    def click_on_yandex_logo(self):
        self.click(LogoPage.YANDEX_LOGO)