import allure
import data

from pages.forms_page import FormsPage


class TestFormsPage:


    @allure.title("Заполнение формы заказа")
    def test_forms_fill_up_order_forms(self, driver):
        forms_page = FormsPage(driver)
        forms_page.open(data.FORMS_URL)
        forms_page.fill_up_first_name_field(data.DATA_FORM.get('first_name'))
        forms_page.fill_up_last_name_field(data.DATA_FORM.get('last_name'))
        forms_page.fill_up_user_adress_field(data.DATA_FORM.get('adress'))
        forms_page.choice_metro_station(data.DATA_FORM.get('metro'))
        forms_page.fill_up_user_number_field(data.DATA_FORM.get('user_number'))
        forms_page.go_to_next_section()
        forms_page.fill_up_delivery_time_field(data.DATA_FORM.get('delivery_time'))

        forms_page.fill_up_comments_field(data.DATA_FORM.get('comments'))