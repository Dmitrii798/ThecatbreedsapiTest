# 🐱 TheCatBreeds API Test Automation

[![API Tests](https://github.com/Dmitrii798/ThecatbreedsapiTest/actions/workflows/tests.yml/badge.svg)](https://github.com/Dmitrii798/ThecatbreedsapiTest/actions/workflows/tests.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-9.1.1-green)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/allure-2.16.1-orange)](https://allurereport.org/)

> Автотесты для API **TheCatAPI** и **ЦБ РФ** с использованием **Python**, **Pytest**, **Requests**, **Allure** и **Faker**.

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

| № | Задание | Файл | Тестов |
|---|---------|------|--------|
| 1 | **Метод "Sources"** — 5 форматов данных (string, number, JSON, dataclass, dict) | `test_data_types.py` | 5 |
| 2 | **Генерация строк** (≥10 символов, буквы, цифры, спецсимволы) | `test_string_generator.py` | 10 |
| 3 | **100 имён** через `faker` (файл + фикстура) | `test_names_generator.py` | 2 |
| 4 | **Валюты и цены** — ЦБ РФ, `parametrize` + XML | `test_currency_rates.py` | 5 |
| — | **Breeds** — дополнительный тест TheCatAPI | `test_breeds.py` | 3 |

**ИТОГО: 25 тестов** ✅

---

## 🎯 Задания

### Задание 1: Метод "Sources" (5 форматов данных)

Проверяет 5 форматов работы с данными на методе `GET /v1/breeds`:

| Формат | Что проверяет | Тест |
|--------|---------------|------|
| **String** | `response.text` — это строка | `test_breeds_string_format` |
| **Number** | `len(breeds)` — число | `test_breeds_number_format` |
| **JSON** | `response.json()` — валидный JSON | `test_breeds_json_format` |
| **Dataclass** | `Breed(**data)` — объект dataclass | `test_breeds_dataclass_format` |
| **Dict** | `{"id": ..., "name": ...}` — словарь | `test_breeds_dict_format` |

### Задание 2: Генерация строк

Генерирует строки с условиями:
- ✅ Минимум **10 символов**
- ✅ Минимум **1 строчная буква**
- ✅ Минимум **1 прописная буква**
- ✅ Минимум **1 цифра**
- ✅ Минимум **1 специальный символ**

Проверяется на **10 итерациях** через `@pytest.mark.parametrize`.

### Задание 3: 100 имён

Генерирует 100 имён через `faker` двумя способами:
- 📄 **Способ 1:** сохранение в файл `data/names.txt`
- 🔧 **Способ 2:** фикстура `names_generated`

Каждое имя — **минимум 2 слова**.

### Задание 4: Валюты и цены (ЦБ РФ)

Проверяет, что курс валют **не опускался ниже** заданного значения за последний год:

| Валюта | Код ЦБ РФ | Мин. цена |
|--------|-----------|-----------|
| USD | R01235 | 50.0 |
| EUR | R01239 | 60.0 |
| AUD | R01010 | 30.0 |
| AZN | R01020A | 30.0 |
| AMD | R01060 | 0.10 |

Использует `@pytest.mark.parametrize` и **XML-запросы** к `cbr.ru`.

---

## 🛠️ Технологии

| Технология | Версия | Назначение |
|-----------|--------|------------|
| **Python** | 3.11+ | Язык |
| **Pytest** | 9.1.1 | Фреймворк тестирования |
| **Requests** | 2.32+ | HTTP-клиент |
| **Allure** | 2.16+ | Отчёты |
| **Faker** | 40.39 | Генерация данных |
| **lxml** | 5.0+ | Парсинг XML |
| **python-dotenv** | 1.0+ | Хранение API-ключа |
| **GitHub Actions** | — | CI/CD |

---

## 📂 Структура проекта

```
ThecatbreedsapiTest/
├── .github/
│   └── workflows/
│       └── tests.yml              # CI/CD
├── checkers/
│   └── checkers.py                # Функции проверок
├── generators/
│   ├── __init__.py
│   ├── currency_gen.py            # Генератор валют
│   ├── names_gen.py               # Генератор имён
│   └── string_gen.py              # Генератор строк
├── data/
│   ├── breeds.json                # Mock-данные пород
│   └── names.txt                  # 100 имён (сгенерированы)
├── tests/
│   └── homework_test_data/
│       ├── test_breeds.py         # 3 теста
│       ├── test_currency_rates.py # 5 тестов
│       ├── test_data_types.py     # 5 тестов
│       ├── test_names_generator.py# 2 теста
│       └── test_string_generator.py# 10 тестов
├── scripts/
│   └── generate_names_file.py     # Скрипт генерации имён
├── conftest.py                    # Фикстуры
├── config.py                      # URL API
├── pytest.ini                     # Настройки pytest
├── requirements.txt               # Зависимости
├── .env                           # API-ключ (не коммитится)
├── .gitignore
└── README.md
```

---

## 🚀 Установка

### 1. Клонируй репозиторий

```bash
git clone https://github.com/Dmitrii798/ThecatbreedsapiTest.git
cd ThecatbreedsapiTest
```

### 2. Создай виртуальное окружение

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```

### 4. Получи API-ключ

Зарегистрируйся на [TheCatAPI](https://thecatapi.com/) и получи бесплатный ключ.

### 5. Создай `.env` файл

```ini
THE_CAT_API_KEY=твой_api_ключ_здесь
```

---

## 🏃 Запуск тестов

### Все тесты

```bash
pytest tests/ -v -s --alluredir=results
```

### Конкретный файл

```bash
pytest tests/homework_test_data/test_currency_rates.py -v -s
```

### Конкретный тест

```bash
pytest "tests/homework_test_data/test_currency_rates.py::TestCurrencyRates::test_currency_rate[R01235-USD-50.0]" -v -s
```

### По метке

```bash
pytest -m homework_test_data -v
```

---

## 📊 Allure-отчёт

### Онлайн-отчёт

📊 **[https://dmitrii798.github.io/ThecatbreedsapiTest/](https://dmitrii798.github.io/ThecatbreedsapiTest/)**

### Локальный просмотр

```bash
# Сгенерировать и открыть отчёт
allure serve results

# Или сгенерировать HTML
allure generate results -o allure-report --clean
allure open allure-report
```

### Что в отчёте

- 📋 **25 тестов** с шагами
- 📎 **Attachments:** XML от ЦБ РФ, сгенерированные строки, имена, JSON пород
- 📈 **Suites:** `homework_test_data`
- 🎯 **Behaviors:** Features/Stories
- 📊 **Graphs:** графики выполнения

---

## 📈 CI/CD

Проект использует **GitHub Actions** для автозапуска тестов:

- ✅ При каждом **push** в `main`
- ✅ При каждом **pull request**
- ✅ Вручную через **workflow_dispatch**

### Пайплайн

```
┌─────────────────────┐
│   Checkout code     │
├─────────────────────┤
│   Set up Python     │
├─────────────────────┤
│   Install deps      │
├─────────────────────┤
│   Install Allure    │
├─────────────────────┤
│   Run tests         │ ← использует secret THE_CAT_API_KEY
├─────────────────────┤
│   Generate report   │
├─────────────────────┤
│   Upload artifact   │
├─────────────────────┤
│   Deploy to Pages   │ → ветка gh-pages
└─────────────────────┘
```

### Бейдж

[![API Tests](https://github.com/Dmitrii798/ThecatbreedsapiTest/actions/workflows/tests.yml/badge.svg)](https://github.com/Dmitrii798/ThecatbreedsapiTest/actions/workflows/tests.yml)

---

## 🧪 Примеры тестов

### Параметризованный тест (валюты)

```python
@pytest.mark.parametrize(
    "val_code, currency_code, min_price",
    get_test_currencies(),
    ids=lambda x: str(x),
)
def test_currency_rate(self, val_code, currency_code, min_price):
    url = f"https://www.cbr.ru/scripts/XML_dynamic.asp?VAL_NM_RQ={val_code}"
    response = requests.get(url)
    # ...
```

### Allure-шаги

```python
with allure.step("Send GET /breeds?limit=1"):
    response = requests.get(f"{url}/breeds?limit=1", headers=headers)
check_status_200(response)

with allure.step("Parse JSON"):
    data = response.json()
    assert "id" in data[0]
```

---

## 📝 Лицензия

MIT

---

## 👤 Автор

**Dmitrii798**
- GitHub: [@Dmitrii798](https://github.com/Dmitrii798)
- Проект: [ThecatbreedsapiTest](https://github.com/Dmitrii798/ThecatbreedsapiTest)

---

## 🙏 Благодарности

- [TheCatAPI](https://thecatapi.com/) — API для тестирования
- [ЦБ РФ](https://www.cbr.ru/) — API курсов валют
- [Allure](https://allurereport.org/) — фреймворк отчётов
- [Faker](https://faker.readthedocs.io/) — генерация данных

---

## ⭐ Если проект был полезен — поставь звезду!

[![Star](https://img.shields.io/github/stars/Dmitrii798/ThecatbreedsapiTest?style=social)](https://github.com/Dmitrii798/ThecatbreedsapiTest)
