import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import BASE_URL


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(options=options)
    browser.get(BASE_URL)
    yield browser
    browser.quit()
