# conftest.py
import os
import pytest
from pathlib import Path
from dotenv import load_dotenv

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
