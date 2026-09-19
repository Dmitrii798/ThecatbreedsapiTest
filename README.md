# 🐱 TheCatBreeds API Test Automation

Автотесты для API TheCatAPI и ЦБ РФ с использованием Python, Pytest, Requests, Allure.

## 📋 Задания

| № | Задание | Файл |
|---|---------|------|
| 1 | Метод Sources (5 форматов) | `test_data_types.py` |
| 2 | Генерация строк | `test_string_generator.py` |
| 3 | 100 имён (faker) | `test_names_generator.py` |
| 4 | Валюты и цены (ЦБ РФ) | `test_currency_rates.py` |

## 🚀 Запуск

```bash
pip install -r requirements.txt
pytest tests/ -v -s --alluredir=results
allure serve results