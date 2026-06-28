import allure
import pytest
import data
from pages.forms_page import FormsPage


class TestFormsPage:

    @allure.title('Создание формы заказа')
    @pytest.mark.parametrize(
        'first_name, last_name, address, metro, user_number, delivery_time, rental_period, color, comments',
        data.DATA_FORM
    )
    def test_create_order(
            self,
            driver,
            first_name,
            last_name,
            address,
            metro,
            user_number,
            delivery_time,
            rental_period,
            color,
            comments
    ):
        forms_page = FormsPage(driver)

        with allure.step('Открытие главной страницы'):
            forms_page.open(data.BASE_URL)

        with allure.step('Принятие cookie'):
            forms_page.accept_cookie()

        with allure.step('Нажатие кнопки заказать'):
            forms_page.go_to_order_button()

        with allure.step('Заполнение первой формы'):
            forms_page.fill_first_form(
                first_name,
                last_name,
                address,
                metro,
                user_number
            )

        with allure.step('Нажатие кнопки далее'):
            forms_page.go_to_further_button()

        with allure.step('Заполнение второй формы'):
            forms_page.fill_second_form(
                delivery_time,
                rental_period,
                color,
                comments
            )

        with allure.step('Подтверждение заказа'):
            forms_page.create_order()

        with allure.step('Просмотр статуса заказа'):
            forms_page.check_status_order()
