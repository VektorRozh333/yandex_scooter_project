import allure
import data

from pages.logo_page import LogoPage


class TestLogoPage:
    @allure.title("Проверка доступности страницы")
    def test_logo_is_avaliable(self, driver):
        logo_page = LogoPage(driver)
        logo_page.open(data.BASE_URL)

    @allure.title("При клике на логотип Самоката происходит переход на главную страницу сайта")
    def test_logo_go_to_main_page(self, driver):
        logo_page = LogoPage(driver)
        logo_page.open(data.BASE_URL)
        logo_page.go_to_main_page()

    @allure.title("При клике на логотип Яндекса происходит переход на стартовую страницу браузера")
    def test_logo_click_on_yandex_logo(self, driver):
        logo_page = LogoPage(driver)
        logo_page.open(data.BASE_URL)
        logo_page.click_on_yandex_logo()