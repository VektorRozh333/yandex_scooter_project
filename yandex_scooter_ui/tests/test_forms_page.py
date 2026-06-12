import allure
import data

from pages.forms_page import FormsPage


class TestFormsPage:
    @allure.title("Проверка доступности страницы")
    def test_forms_is_avaliable(self, driver):
        forms_page = FormsPage(driver)
        forms_page.open(data.BASE_URL)

    