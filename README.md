# 🐱 TheCatBreeds API Test Automation

[![API Tests](https://github.com/Dmitrii798/ThecatbreedsapiTest/actions/workflows/tests.yml/badge.svg)](https://github.com/Dmitrii798/ThecatbreedsapiTest/actions/workflows/tests.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-9.1.1-green)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/allure-2.16.1-orange)](https://allurereport.org/)

> Автотесты для API **TheCatAPI** и **ЦБ РФ** с использованием **Python**, **Pytest**, **Requests**, **Allure** и *
*Faker**.

📊 **[Отчёт Allure онлайн](https://dmitrii798.github.io/ThecatbreedsapiTest/)** — опубликован на GitHub Pages.

---

## 📋 Содержание

- [Описание](#-описание)
- [Задания](#-задания)
- [Технологии](#-технологии)
- [Структура проекта](#-структура-проекта)
- [Установка](#-установка)
- [Запуск тестов](#-запуск-тестов)
- [Allure-отчёт](#-allure-отчёт)
- [CI/CD](#-cicd)
- [Автор](#-автор)

---

## 📖 Описание

Проект содержит **25 автотестов**, покрывающих:

| № | Задание                                 | Файл                       | Тестов |
|---|-----------------------------------------|----------------------------|--------|
| 1 | **Метод "Sources"** — 5 форматов данных | `test_data_types.py`       | 5      |
| 2 | **Генерация строк**                     | `test_string_generator.py` | 10     |
| 3 | **100 имён** через `faker`              | `test_names_generator.py`  | 2      |
| 4 | **Валюты и цены** (ЦБ РФ)               | `test_currency_rates.py`   | 5      |
| — | **Breeds** (доп.)                       | `test_breeds.py`           | 3      |

**ИТОГО: 25 тестов** ✅

---

## 🎯 Задания

### Задание 1: Метод "Sources" (5 форматов данных)

Проверяет 5 форматов работы с данными на `GET /v1/breeds`:

| Формат        | Что проверяет                        |
|---------------|--------------------------------------|
| **String**    | `response.text` — это строка         |
| **Number**    | `len(breeds)` — число                |
| **JSON**      | `response.json()` — валидный JSON    |
| **Dataclass** | `Breed(**data)` — объект dataclass   |
| **Dict**      | `{"id": ..., "name": ...}` — словарь |

### Задание 2: Генерация строк

- ✅ Минимум **10 символов**
- ✅ Минимум **1 строчная буква**
- ✅ Минимум **1 прописная буква**
- ✅ Минимум **1 цифра**
- ✅ Минимум **1 специальный символ**

Проверяется на **10 итерациях** через `@pytest.mark.parametrize`.

### Задание 3: 100 имён

Генерирует 100 имён через `faker` двумя способами:

- 📄 **Способ 1:** файл `data/names.txt`
- 🔧 **Способ 2:** фикстура `names_generated`

### Задание 4: Валюты и цены (ЦБ РФ)

Проверяет, что курс валют **не опускался ниже** порога:

| Валюта | Код ЦБ РФ | Мин. цена |
|--------|-----------|-----------|
| USD    | R01235    | 50.0      |
| EUR    | R01239    | 60.0      |
| AUD    | R01010    | 30.0      |
| AZN    | R01020A   | 30.0      |
| AMD    | R01060    | 0.10      |

---

## 🛠️ Технологии

| Технология        | Версия | Назначение       |
|-------------------|--------|------------------|
| **Python**        | 3.11+  | Язык             |
| **Pytest**        | 9.1.1  | Фреймворк        |
| **Requests**      | 2.32+  | HTTP-клиент      |
| **Allure**        | 2.16+  | Отчёты           |
| **Faker**         | 40.39  | Генерация данных |
| **lxml**          | 5.0+   | Парсинг XML      |
| **python-dotenv** | 1.0+   | API-ключ         |

---

## 📂 Структура проекта

```
ThecatbreedsapiTest/
├── .github/workflows/tests.yml    # CI/CD
├── checkers/checkers.py           # Проверки
├── generators/                    # Генераторы данных
│   ├── currency_gen.py
│   ├── names_gen.py
│   └── string_gen.py
├── data/
│   ├── breeds.json
│   └── names.txt
├── tests/homework_test_data/      # 25 тестов
├── scripts/generate_names_file.py
├── conftest.py                    # Фикстуры
├── config.py                      # URL API
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🚀 Установка

```bash
# 1. Клонируй
git clone https://github.com/Dmitrii798/ThecatbreedsapiTest.git
cd ThecatbreedsapiTest

# 2. Виртуальное окружение
python -m venv .venv
.venv\Scripts\activate  # Windows

# 3. Зависимости
pip install -r requirements.txt

# 4. Создай .env
echo "THE_CAT_API_KEY=твой_ключ" > .env
```

---

## 🏃 Запуск тестов

```bash
# Все тесты
pytest tests/ -v -s --alluredir=results

# Конкретный файл
pytest tests/homework_test_data/test_currency_rates.py -v -s

# Конкретный тест
pytest "tests/homework_test_data/test_currency_rates.py::TestCurrencyRates::test_currency_rate[R01235-USD-50.0]" -v -s
```

---

## 📊 Allure-отчёт

📊 **[https://dmitrii798.github.io/ThecatbreedsapiTest/](https://dmitrii798.github.io/ThecatbreedsapiTest/)**

Локально:

```bash
allure serve results
```

---

## 📈 CI/CD

GitHub Actions автоматически:

- ✅ Запускает тесты на **push** в `main`
- ✅ Генерирует **Allure-отчёт**
- ✅ Публикует на **GitHub Pages**

[![API Tests](https://github.com/Dmitrii798/ThecatbreedsapiTest/actions/workflows/tests.yml/badge.svg)](https://github.com/Dmitrii798/ThecatbreedsapiTest/actions/workflows/tests.yml)

---

## 👤 Автор

**Dmitrii798**

- GitHub: [@Dmitrii798](https://github.com/Dmitrii798)
- Проект: [ThecatbreedsapiTest](https://github.com/Dmitrii798/ThecatbreedsapiTest)

---

## 🙏 Благодарности

- [TheCatAPI](https://thecatapi.com/)
- [ЦБ РФ](https://www.cbr.ru/)
- [Allure](https://allurereport.org/)
- [Faker](https://faker.readthedocs.io/)

---

⭐ **Если проект был полезен — поставь звезду!**