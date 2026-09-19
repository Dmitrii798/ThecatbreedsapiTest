# tests/homework_test_data/test_breeds.py
import json
import allure
import pytest
import requests

from checkers.checkers import check_status_200, check_response_length
from config import url


@allure.suite("homework_test_data")
class TestBreeds:
    """Тесты для метода /breeds (аналог /sources)."""

    @pytest.mark.homework_test_data
    @allure.title("Test first breed name")
    def test_breeds_first_name(self, headers: dict) -> None:
        with allure.step("Send GET /breeds?limit=1"):
            response = requests.get(
                f"{url}/breeds?limit=1",
                headers=headers
            )
        check_status_200(response)
        assert response.json()[0]["name"], "Name is empty"

    @pytest.mark.homework_test_data
    @allure.title("Test breeds limit filter")
    def test_breeds_limit_filter(self, headers: dict) -> None:
        limit = 10
        with allure.step(f"Send GET /breeds?limit={limit}"):
            response = requests.get(
                f"{url}/breeds?limit={limit}",
                headers=headers
            )
        check_status_200(response)
        check_response_length(response, len_my=limit)

    @pytest.mark.homework_test_data
    @allure.title("Test all breeds")
    def test_breeds_all(self, headers: dict) -> None:
        with allure.step("Send GET /breeds"):
            response = requests.get(
                f"{url}/breeds",
                headers=headers
            )
        check_status_200(response)
        data = response.json()
        assert isinstance(data, list), "Not a list"
        assert len(data) > 0, "Empty"

        # Сохраняем в файл для мок-данных
        with open("data/breeds.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
           