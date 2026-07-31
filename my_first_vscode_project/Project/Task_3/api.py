import allure
import requests

from helpers import generate_user_data
from urls import INGREDIENTS_URL, ORDERS_URL, REGISTER_URL, USER_URL


@allure.step('Регистрация нового пользователя через API')
def register_new_user():
    user_data = generate_user_data()
    response = requests.post(REGISTER_URL, json=user_data)
    access_token = None
    refresh_token = None
    if response.status_code == 200:
        body = response.json()
        access_token = body.get('accessToken')
        refresh_token = body.get('refreshToken')
    return user_data, access_token, refresh_token


@allure.step('Удаление пользователя через API')
def delete_user(access_token):
    if not access_token:
        return None
    return requests.delete(USER_URL, headers={'Authorization': access_token})


@allure.step('Получение id ингредиентов для заказа')
def get_ingredient_ids():
    response = requests.get(INGREDIENTS_URL)
    ingredients = response.json()['data']
    bun = next(item['_id'] for item in ingredients if item['type'] == 'bun')
    filling = next(item['_id'] for item in ingredients if item['type'] != 'bun')
    return [bun, filling]


@allure.step('Создание заказа через API')
def create_order(access_token, ingredients=None):
    if ingredients is None:
        ingredients = get_ingredient_ids()
    return requests.post(
        ORDERS_URL,
        json={'ingredients': ingredients},
        headers={'Authorization': access_token},
    )
