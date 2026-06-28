import allure
import data
from pages.logo_page import LogoPage
from selenium.webdriver.support.ui import WebDriverWait


class TestLogoPage:
    
    @allure.title("Проверка перехода через кнопки заказа и логотипа")
    def test_logo_is_avaliable(self, driver):
        logo_page = LogoPage(driver)

        with allure.step('Открытие главной страницы'):
            logo_page.open(data.BASE_URL)

        with allure.step('Принятие cookie'):
            logo_page.accept_cookie()

        with allure.step('Переход через верхнюю кнопку заказа'):
            logo_page.click_on_order_logo()

        with allure.step('Нажатие на логотип Самоката'):
            logo_page.click_on_scooter_logo()

        with allure.step('Проверка перехода на главную страницу'):
            assert driver.current_url == data.BASE_URL


    @allure.title("При клике на логотип Яндекса происходит переход на стартовую страницу браузера")
    def test_logo_click_on_yandex_logo(self, driver):
        logo_page = LogoPage(driver)

        with allure.step('Открытие главной страницы'):
            logo_page.open(data.BASE_URL)

        with allure.step('Принятие cookie'):
            logo_page.accept_cookie()

        with allure.step('Клик на логотип Яндекса'):
            logo_page.click_on_yandex_logo()

        with allure.step('Ожидание открытия новой вкладки'):
            WebDriverWait(driver, 10).until(
                lambda d: len(d.window_handles) > 1
            )

        with allure.step('Переключение на новую вкладку'):
            driver.switch_to.window(driver.window_handles[1])

        with allure.step('Ожидание загрузки страницы'):
            WebDriverWait(driver, 15).until(
                lambda d: d.current_url != 'about:blank'
            )

        with allure.step('Проверка перехода'):
            print(driver.current_url)
            assert 'ya.ru' in driver.current_url.lower() or \
                'dzen' in driver.current_url.lower()
