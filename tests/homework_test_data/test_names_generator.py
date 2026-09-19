# tests/homework_test_data/test_names_generator.py
import allure
import pytest


@allure.suite("homework_test_data")
class TestNamesGenerator:

    @pytest.mark.homework_test_data
    @allure.title("Names from file: 100 names, each >= 2 words")
    def test_names_from_file(self, names_from_file: list[str]) -> None:
        """Способ 1: читаем имена из файла."""
        with allure.step(f"Check count = 100 (got {len(names_from_file)})"):
            assert len(names_from_file) == 100, \
                f"Expected 100, got {len(names_from_file)}"

        with allure.step("Check each name has >= 2 words"):
            for name in names_from_file:
                words = name.split()
                assert len(words) >= 2, \
                    f"Name '{name}' has only {len(words)} word(s)"

        allure.attach(
            "\n".join(names_from_file),
            name="Names from file",
            attachment_type=allure.attachment_type.TEXT
        )

    @pytest.mark.homework_test_data
    @allure.title("Generated names: 100 names, each >= 2 words")
    def test_names_generated(self, names_generated: list[str]) -> None:
        """Способ 2: генерируем имена на лету."""
        with allure.step(f"Check count = 100 (got {len(names_generated)})"):
            assert len(names_generated) == 100, \
                f"Expected 100, got {len(names_generated)}"

        with allure.step("Check each name has >= 2 words"):
            for name in names_generated:
                words = name.split()
                assert len(words) >= 2, \
                    f"Name '{name}' has only {len(words)} word(s)"

        allure.attach(
            "\n".join(names_generated),
            name="Generated names",
            attachment_type=allure.attachment_type.TEXT
        )
