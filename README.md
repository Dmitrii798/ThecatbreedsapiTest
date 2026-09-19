# 🐱 TheCatBreeds API Test Automation

Автотесты для API TheCatAPI и ЦБ РФ с использованием **Python**, **Pytest**, **Requests**, **Allure**.

[![API Tests](https://github.com/Dmitrii798/ThecatbreedsapiTest/actions/workflows/tests.yml/badge.svg)](https://github.com/Dmitrii798/ThecatbreedsapiTest/actions/workflows/tests.yml)

📊 **[Отчёт Allure](https://dmitrii798.github.io/ThecatbreedsapiTest/)** — доступен онлайн!

---

## 📋 Задания

| № | Задание | Файл | Тестов |
|---|---------|------|--------|
| 1 | Метод Sources (5 форматов) | `test_data_types.py` | 5 |
| 2 | Генерация строк | `test_string_generator.py` | 10 |
| 3 | 100 имён (faker) | `test_names_generator.py` | 2 |
| 4 | Валюты и цены (ЦБ РФ) | `test_currency_rates.py` | 5 |
| — | Breeds (доп.) | `test_breeds.py` | 3 |

**ИТОГО: 25 тестов**

---

## 🛠️ Технологии

- **Python 3.11+**
- **Pytest** — фреймворк
- **Requests** — HTTP-клиент
- **Allure** — отчёты
- **Faker** — генерация данных
- **lxml** — парсинг XML
- **python-dotenv** — хранение API-ключа

---

## 🚀 Установка

```bash
git clone https://github.com/Dmitrii798/ThecatbreedsapiTest.git
cd ThecatbreedsapiTest
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Создай `.env`:

```ini
THE_CAT_API_KEY=твой_ключ
```

---

## 🏃 Запуск

```bash
# Все тесты
pytest tests/ -v -s --alluredir=results

# Конкретный файл
pytest tests/homework_test_data/test_currency_rates.py -v -s

# Отчёт Allure
allure serve results
```

---

## 📂 Структура

```
ThecatbreedsapiTest/
├── .github/workflows/tests.yml
├── checkers/
├── generators/
├── tests/homework_test_data/
├── conftest.py
├── config.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 👤 Автор

**Dmitrii798**