import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from api import create_order, delete_user, register_new_user
from urls import MAIN_URL


@pytest.fixture(params=['chrome', 'firefox'], ids=['chrome', 'firefox'])
def driver(request):
    """Запускает тест в Chrome и Firefox."""
    headless = os.getenv('HEADLESS', '').lower() in {'1', 'true', 'yes'}

    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        if headless:
            options.add_argument('--headless=new')
        browser = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        if headless:
            options.add_argument('-headless')
        browser = webdriver.Firefox(options=options)

    if not headless:
        browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def new_user():
    """Создаёт пользователя перед тестом и удаляет после."""
    user_data, access_token, refresh_token = register_new_user()
    yield {
        'user_data': user_data,
        'access_token': access_token,
        'refresh_token': refresh_token,
    }
    delete_user(access_token)


@pytest.fixture
def authorized_driver(driver, new_user):
    """Открывает приложение с токенами авторизованного пользователя."""
    driver.get(MAIN_URL)
    driver.execute_script(
        "window.localStorage.setItem('accessToken', arguments[0]);",
        new_user['access_token'],
    )
    driver.execute_script(
        "window.localStorage.setItem('refreshToken', arguments[0]);",
        new_user['refresh_token'],
    )
    driver.refresh()
    return driver


@pytest.fixture
def user_with_order(new_user):
    """Создаёт пользователя и заказ через API."""
    create_order(new_user['access_token'])
    return new_user
