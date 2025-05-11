import pytest
from selenium import webdriver
from urls import Main_URL
from selenium.webdriver.chrome.options import Options


@pytest.fixture(params = ['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = Options()
        driver = webdriver.Chrome(options=options)

    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("dom.events.asyncClipboard.read", True)
        options.set_preference("dom.events.testing.asyncClipboard", True)
        driver = webdriver.Firefox(options=options)

    driver.get(Main_URL)
    yield driver
    driver.quit()

