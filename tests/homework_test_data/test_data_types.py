# tests/homework_test_data/test_data_types.py
import json
import allure
import pytest
import requests
from dataclasses import dataclass, asdict

from checkers.checkers import check_status_200, check_response_length
from config import url


# ==================== DATACLASS ====================

@dataclass
class Breed:
    id: str
    name: str
    origin: str | None = None
    temperament: str | None = None
    life_span: str | None = None
    wikipedia_url: str | None = None


# ==================== TESTS ====================

@allure.suite("homework_test_data")
class TestDataTypes:
    """Проверяет 5 форматов данных на методе /breeds."""

    # ---------- 1. STRING ----------

    @pytest.mark.homework_test_data
    @allure.title("Test breeds as string")
    def test_breeds_string_format(self, headers: dict) -> None:
        """Формат 1: строка (raw JSON как строка)."""
        response = requests.get(f"{url}/breeds?limit=1", headers=headers)
        check_status_200(response)

        raw_text = response.text
        assert isinstance(raw_text, str)
        assert len(raw_text) > 0
        assert '"name"' in raw_text
        with allure.step("Send GET /breeds?limit=1"):
            response = requests.get(
                f"{url}/breeds?limit=1",
                headers=headers
            )
        check_status_200(response)

        with allure.step("Check response is a string"):
            raw_text = response.text
            assert isinstance(raw_text, str), "Response is not a string"
            assert len(raw_text) > 0, "Response is empty"
            assert '"name"' in raw_text, "No 'name' field in response"

        allure.attach(
            raw_text,
            name="Raw string",
            attachment_type=allure.attachment_type.TEXT
        )

    # ---------- 2. NUMBER ----------

    @pytest.mark.homework_test_data
    @allure.title("Test breeds as number")
    def test_breeds_number_format(self, headers: dict) -> None:
        """Формат 2: число (количество пород, limit)."""
        with allure.step("Send GET /breeds?limit=5"):
            response = requests.get(
                f"{url}/breeds?limit=5",
                headers=headers
            )
        check_status_200(response)

        with allure.step("Check count is a number"):
            breeds = response.json()
            count = len(breeds)
            assert isinstance(count, int), f"Count is not int: {type(count)}"
            assert count > 0, "Count is 0"
            assert count <= 5, f"Count {count} > limit 5"

        allure.attach(
            f"Count: {count}",
            name="Number",
            attachment_type=allure.attachment_type.TEXT
        )

    # ---------- 3. JSON ----------

    @pytest.mark.homework_test_data
    @allure.title("Test breeds as JSON")
    def test_breeds_json_format(self, headers: dict) -> None:
        """Формат 3: JSON (парсим ответ как JSON)."""
        with allure.step("Send GET /breeds?limit=1"):
            response = requests.get(
                f"{url}/breeds?limit=1",
                headers=headers
            )
        check_status_200(response)

        with allure.step("Parse JSON"):
            data = response.json()
            assert isinstance(data, list), "Response is not a list"
            assert len(data) > 0, "Empty list"
            assert "id" in data[0], "No 'id' field"
            assert "name" in data[0], "No 'name' field"

        allure.attach(
            json.dumps(data, indent=2),
            name="JSON",
            attachment_type=allure.attachment_type.JSON
        )

    # ---------- 4. DATACLASS ----------

    @pytest.mark.homework_test_data
    @allure.title("Test breeds as dataclass")
    def test_breeds_dataclass_format(self, headers: dict) -> None:
        """Формат 4: dataclass."""
        with allure.step("Send GET /breeds?limit=1"):
            response = requests.get(
                f"{url}/breeds?limit=1",
                headers=headers
            )
        check_status_200(response)

        with allure.step("Convert to Breed dataclass"):
            data = response.json()[0]
            breed = Breed(
                id=data["id"],
                name=data["name"],
                origin=data.get("origin"),
                temperament=data.get("temperament"),
                life_span=data.get("life_span"),
                wikipedia_url=data.get("wikipedia_url"),
            )

        with allure.step("Check dataclass fields"):
            assert isinstance(breed, Breed)
            assert breed.id, "Empty id"
            assert breed.name, "Empty name"

        allure.attach(
            json.dumps(asdict(breed), indent=2),
            name="Dataclass",
            attachment_type=allure.attachment_type.JSON
        )

    # ---------- 5. DICT ----------

    @pytest.mark.homework_test_data
    @allure.title("Test breeds as dict")
    def test_breeds_dict_format(self, headers: dict) -> None:
        """Формат 5: словарь."""
        with allure.step("Send GET /breeds?limit=1"):
            response = requests.get(
                f"{url}/breeds?limit=1",
                headers=headers
            )
        check_status_200(response)

        with allure.step("Convert to dict"):
            data = response.json()[0]
            breed_dict = {
                "id": data.get("id"),
                "name": data.get("name"),
                "origin": data.get("origin"),
            }

        with allure.step("Check dict"):
            assert isinstance(breed_dict, dict), "Not a dict"
            assert breed_dict["id"], "Empty id"
            assert breed_dict["name"], "Empty name"
            assert breed_dict["origin"] is not None, "Empty origin"

        allure.attach(
            json.dumps(breed_dict, indent=2),
            name="Dict",
            attachment_type=allure.attachment_type.JSON
        )

@pytest.fixture
def headers() -> dict:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("THE_CAT_API_KEY")
    return {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
