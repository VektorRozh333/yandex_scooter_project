import chromedriver_autoinstaller
import pytest
from selenium import webdriver
# не забыть указать путь к конфтесту

@pytest.fixture(scope='function')
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
