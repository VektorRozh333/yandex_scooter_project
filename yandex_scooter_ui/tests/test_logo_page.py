import allure
import data

from pages.logo_page import LogoPage


class TestLogoPage:
    @allure.title("Проверка перехода через кнопки заказа и логотипа")
    def test_logo_is_avaliable(self, driver):
        logo_page = LogoPage(driver)

        with allure.step('Открытие главной страницы'):
            logo_page.open(data.BASE_URL)

        with allure.step('Принятие cookie'):
            logo_page.accept_cookie()

        with allure.step('Переход через верхнюю кнопку заказа'):
            logo_page.go_to_main_page_top_button()

        with allure.step('Переход через нижнюю кнопку заказа'):
            logo_page.go_to_main_page_bottom_button()


    @allure.title("При клике на логотип Яндекса происходит переход на стартовую страницу браузера")
    def test_logo_click_on_yandex_logo(self, driver):
        logo_page = LogoPage(driver)

        with allure.step('Открытие главной страницы'):
            logo_page.open(data.BASE_URL)

        with allure.step('Принятие cookie'):
            logo_page.accept_cookie()

        with allure.step('Клик на логотип Яндекса'):
            logo_page.click_on_yandex_logo()
