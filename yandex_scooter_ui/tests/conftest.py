import chromedriver_autoinstaller
import allure
import pytest

from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    
    chromedriver_autoinstaller.install()
    with allure.step('Запуск браузера'):
        driver = webdriver.Chrome()
        driver.maximize_window()
    yield driver

    with allure.step('Закрытие браузера'):
        driver.quit()
    