import allure
import pytest
import data
import time

from pages.forms_page import FormsPage


class TestFormsPage:

    @allure.title("Заполнение формы заказа")
    @pytest.mark.parametrize(
        'first_name, last_name, address, metro, user_number',
        data.DATA_FORM
    )

    @allure.title('Позитивный тест создания заказа')
    def test_create_order(
            self,
            driver,
            first_name,
            last_name,
            address,
            metro,
            user_number
    ):
        forms_page = FormsPage(driver)

        with allure.step('Открытие главной страницы'):
            forms_page.open(data.BASE_URL)

        with allure.step('Принятие cookie'):
            forms_page.accept_cookie()
        time.sleep(3)
        with allure.step('Нажатие кнопки заказать'):
            forms_page.go_to_order_button()
        time.sleep(3)
        with allure.step('Заполнение первой формы'):
            forms_page.fill_first_form(
                first_name,
                last_name,
                address,
                metro,
                user_number
            )
        time.sleep(3)
        with allure.step('Нажатие кнопки далее'):
            forms_page.go_to_further_button()