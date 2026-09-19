# tests/homework_test_data/test_currency_rates.py
import allure
import pytest
import requests
from lxml import etree

from generators.currency_gen import get_test_currencies


@allure.suite("homework_test_data")
class TestCurrencyRates:

    @pytest.mark.homework_test_data
    @allure.title("Currency {currency_code} did not drop below {min_price}")
    @allure.description(
        "Проверяет, что курс валюты не опускался ниже заданного значения "
        "за последний год. Использует parametrize и XML-запросы к ЦБ РФ."
    )
    @pytest.mark.parametrize(
        "val_code, currency_code, min_price",
        get_test_currencies(),
        ids=lambda x: str(x),
    )
    def test_currency_rate(
            self,
            val_code: str,
            currency_code: str,
            min_price: float,
    ) -> None:
        # Период: последний год
        url = (
            f"https://www.cbr.ru/scripts/XML_dynamic.asp?"
            f"date_req1=01/01/2024&date_req2=31/12/2024"
            f"&VAL_NM_RQ={val_code}"
        )

        with allure.step(f"Send GET to CBR for {currency_code}"):
            response = requests.get(url)

        with allure.step("Check status 200"):
            assert response.status_code == 200, \
                f"Got {response.status_code}: {response.text[:200]}"

        with allure.step("Check Content-Type is XML"):
            content_type = response.headers.get("Content-Type", "")
            assert "xml" in content_type.lower() or response.content.startswith(b"<?xml"), \
                f"Expected XML, got {content_type}"

        with allure.step("Parse XML"):
            root = etree.fromstring(response.content)
            records = root.findall("Record")
            assert len(records) > 0, f"No records for {currency_code}"

        with allure.step(f"Check all prices >= {min_price}"):
            min_found = float("inf")
            min_date = None

            for record in records:
                value = record.findtext("Value")
                value_float = float(value.replace(",", "."))
                date = record.get("Date")

                if value_float < min_found:
                    min_found = value_float
                    min_date = date

            assert min_found >= min_price, (
                f"{currency_code} dropped below {min_price}: "
                f"min = {min_found} on {min_date}"
            )

            allure.attach(
                f"Currency: {currency_code}\n"
                f"Min price: {min_found} on {min_date}\n"
                f"Threshold: {min_price}\n"
                f"Records: {len(records)}",
                name=f"{currency_code} stats",
                attachment_type=allure.attachment_type.TEXT
            )

        allure.attach(
            response.text,
            name=f"{currency_code} XML",
            attachment_type=allure.attachment_type.XML
        )
       