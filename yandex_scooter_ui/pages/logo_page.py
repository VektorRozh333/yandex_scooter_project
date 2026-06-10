import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogoPage(BasePage):
    YANDEX_LOGO = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
    SCOOTER_LOGO = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    TEST_TRANSITION = (By.XPATH, ".//button[@class='Button_Button__ra12g']")

    @allure.step("Проверка перехода на главную страницу Самоката")
    def go_to_main_page(self):
        self.click(LogoPage.TEST_TRANSITION)
        self.click(LogoPage.SCOOTER_LOGO)

    @allure.step("Проверка кликабельности логотипа Яндекса")
    def click_on_yandex_logo(self):
        self.click(LogoPage.YANDEX_LOGO)