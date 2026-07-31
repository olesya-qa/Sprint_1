# Stellar Burgers UI Tests

UI-автотесты веб-приложения [Stellar Burgers](https://qa-stellarburgers.education-services.ru).

## Стек

- Python 3
- pytest
- Selenium WebDriver
- requests
- allure-pytest
- Page Object Model

## Установка

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Нужны установленные Google Chrome и Mozilla Firefox.

## Запуск тестов

```bash
pytest tests/ --alluredir=allure-results
```

Тесты запускаются в Chrome и Firefox.

## Allure-отчёт

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Структура

- `locators/` — локаторы элементов
- `pages/` — Page Object классы
- `tests/` — тесты по функциональности
- `api.py` — создание и удаление тестовых пользователей через API
