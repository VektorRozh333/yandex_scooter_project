import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogoPage(BasePage):
    YANDEX_LOGO = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
    SCOOTER_LOGO = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    TEST_TRANSITION_TOP = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    TEST_TRANSITION_BOTTOM = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')


    @allure.step('Принятие cookies')
    def accept_cookie(self):
        self.click(self.COOKIE_BUTTON)


    @allure.step("Проверка перехода на главную страницу Самоката через верхнюю кнопку")
    def go_to_main_page_top_button(self):
        self.click(LogoPage.TEST_TRANSITION_TOP)
        self.click(LogoPage.SCOOTER_LOGO)


    @allure.step("Проверка перехода на главную страницу Самоката через нижнюю кнопку")
    def go_to_main_page_bottom_button(self):
        self.scroll_to_element(LogoPage.TEST_TRANSITION_BOTTOM)
        self.click(LogoPage.TEST_TRANSITION_BOTTOM)
        self.click(LogoPage.SCOOTER_LOGO)


    @allure.step("Проверка кликабельности логотипа Яндекса")
    def click_on_yandex_logo(self):
        self.click(LogoPage.YANDEX_LOGO)