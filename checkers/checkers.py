# checkers/checkers.py
import allure
import datetime


def check_status(response, status_code: int) -> None:
    """Универсальная проверка статус-кода."""
    with allure.step(f"Check status code {status_code}"):
        assert response.status_code == status_code, \
            f"Expected {status_code}, got {response.status_code}: {response.text}"


def check_status_200(response) -> None:
    """Проверка статус-кода 200."""
    check_status(response, 200)


def check_status_201(response) -> None:
    """Проверка статус-кода 201."""
    check_status(response, 201)


def check_status_400(response) -> None:
    """Проверка статус-кода 400."""
    check_status(response, 400)


def check_status_401(response) -> None:
    """Проверка статус-кода 401."""
    check_status(response, 401)


def check_not_empty(response) -> None:
    """Проверка, что ответ не пустой."""
    with allure.step("Check that response is not empty"):
        data = response.json()
        assert data is not None, "Response is None"
        assert len(data) > 0, "Response is empty"


def check_response_length(response, len_my: int) -> None:
    """Проверка длины ответа."""
    with allure.step(f"Check response length <= {len_my}"):
        data = response.json()
        assert len(data) <= len_my, \
            f"Length {len(data)} > {len_my}"


def check_dates_order_desc(response) -> None:
    """Проверка сортировки дат по убыванию."""
    with allure.step("Check dates order DESC"):
        data = response.json()
        dates = [item.get("created_at") for item in data if item.get("created_at")]
        assert len(dates) > 0, "No dates found"

        parsed = []
        for d in dates:
            clean = d.replace("Z", "+00:00")
            parsed.append(datetime.datetime.fromisoformat(clean))

        for i in range(len(parsed) - 1):
            assert parsed[i] >= parsed[i + 1], \
                f"Dates not DESC: {parsed[i]} < {parsed[i + 1]}"


def check_x_api_key(response) -> None:
    """Проверка наличия x-api-key в запросе."""
    with allure.step("Check x-api-key in request headers"):
        assert "x-api-key" in response.request.headers, \
            "No x-api-key in request headers"


def check_status_400_duplicate(response) -> None:
    """Проверка ошибки DUPLICATE_FAVOURITE."""
    with allure.step("Check status 400 (duplicate)"):
        assert response.status_code == 400, \
            f"Expected 400, got {response.status_code}"
       