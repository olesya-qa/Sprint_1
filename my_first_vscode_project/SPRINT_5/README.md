# Проект автоматизации UI-тестов сервиса «Доска»

Автотесты проверяют регистрацию, авторизацию, выход из системы и создание объявлений на сайте [Доска](https://qa-desk.education-services.ru/).

Основа для написания автотестов — фреймворк pytest и библиотека Selenium WebDriver. Тесты запускаются в Google Chrome.

## Установка

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest -v tests
```
