# conftest.py
import os
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def headers() -> dict:
    api_key = os.getenv("THE_CAT_API_KEY")
    if not api_key:
        pytest.fail("THE_CAT_API_KEY not found in .env")
    return {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }


# conftest.py
import pytest
from generators.names_gen import generate_names


@pytest.fixture(scope="session")
def names_from_file():
    """Читает имена из текстового файла (способ 1)."""
    with open("data/names.txt", "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]
    return names


@pytest.fixture(scope="session")
def names_generated():
    """Генерирует имена на лету (способ 2)."""
    return generate_names(100)
