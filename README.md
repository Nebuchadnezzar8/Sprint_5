# Sprint_5

# Описание проекта

Автотесты для сервиса Stellar Burgers

## Структура проекта

- `helpers/`: Содержит вспомогательные модули, такие как генераторы данных, локаторы и URL.
  - `data_generators.py`: Генерация тестового email
  - `user_data.py`: тестовые данные для авторизованного пользователя
  - `locators.py`: Определение локаторов для элементов веб-страниц.
  - `urls.py`: Хранение URL-адресов, используемых в тестах.

- `test/`: Содержит тесты и конфигурационные файлы.
  - `conftest.py`: Фикстуры и общие настройки для тестов.
  - `test_constructor_navigation.py`: Тесты навигации для конструктора
  - `test_registration.py`: Тесты для регистрации пользователей.
  - `test_user_authentication.py`: Тесты аутентификации пользователей.
  - `test_user_navigation.py`: Тесты пользовательской навигации.

## Требования

  - Python 3.x
  - Selenium WebDriver
  - Pytest

## Установка

1. Клонируйте репозиторий:

git clone https://github.com/Nebuchadnezzar8/Sprint_5.git

2. Установите зависимости:

pip install -r requirements.txt


## Запуск тестов

  - Для запуска всех тестов выполните:
  - pytest