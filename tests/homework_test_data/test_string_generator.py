# tests/homework_test_data/test_string_generator.py
import string
import allure
import pytest

from generators.string_gen import generate_string


@allure.suite("homework_test_data")
class TestStringGenerator:

    @pytest.mark.homework_test_data
    @allure.title("Generated string meets all conditions")
    @pytest.mark.parametrize("iteration", range(10))
    def test_generated_string(self, iteration: int) -> None:
        """Проверяет, что сгенерированная строка соответствует всем условиям."""
        s = generate_string(min_length=12)

        with allure.step(f"String: {s}"):
            allure.attach(
                s,
                name="Generated string",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Check length >= 10"):
            assert len(s) >= 10, f"Length < 10: {len(s)}"

        with allure.step("Check has lowercase letter"):
            assert any(c.islower() for c in s), "No lowercase letter"

        with allure.step("Check has uppercase letter"):
            assert any(c.isupper() for c in s), "No uppercase letter"

        with allure.step("Check has digit"):
            assert any(c.isdigit() for c in s), "No digit"

        with allure.step("Check has special char"):
            assert any(c in string.punctuation for c in s), "No special char"

        with allure.step("Check no spaces"):
            assert " " not in s, "String contains spaces"
           