import pytest
from selenium import webdriver
from urls import Main_URL

@pytest.fixture(params = ['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()

    driver.get(Main_URL)
    yield driver
    driver.quit()

