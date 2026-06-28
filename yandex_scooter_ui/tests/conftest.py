import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    
    with allure.step('Запуск браузера'):
        driver = webdriver.Firefox()
        driver.maximize_window()
    yield driver

    with allure.step('Закрытие браузера'):
        driver.quit()
    