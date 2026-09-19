# conftest.py
import os
import pytest
from pathlib import Path
from dotenv import load_dotenv

from generators.names_gen import generate_names

# Явно указываем путь к .env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)


@pytest.fixture
def headers() -> dict:
    api_key = os.getenv("THE_CAT_API_KEY")
    if not api_key:
        pytest.fail(
            f"THE_CAT_API_KEY is not set. "
            f"Checked .env at: {env_path} (exists: {env_path.exists()}). "
            f"On CI: ensure secret THE_CAT_API_KEY is set in GitHub."
        )
    return {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }


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
