from fastapi import FastAPI, Query, Path
from typing import Annotated
import requests
from decimal import Decimal
import json
from fastapi.middleware.cors import CORSMiddleware

from src.functions import process_currency_req
from src.enums import Currency_type

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def home():
    return {'message': 'Welcome!'}

@app.get('/get_currency_rates')
async def get_currency_rates():
    res = requests.get("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt")
    currency = process_currency_req(res)
    return { "currency_rates": currency }

@app.get('/convert_amount_from_czk/{currency_type}')
async def convert_from_czk(
    currency_type: Annotated[Currency_type, Path(description="The currency you want to transfer money to")],
    amount: Annotated[Decimal, Query(description="The amount of CZK you want to convert")]
    ):
    res = await get_currency_rates()
    currency = res.get("currency_rates")
    rate = currency.get(currency_type.value)
    return { "converted_amount": amount/rate }

@app.get('/name_day')
async def get_nameday():
    res = requests.get("https://nameday.abalin.net/api/V1/today")
    data = json.loads(res.text)
    return { "nameday": data.get("nameday").get("cz") }

@app.get('/currency_types')
async def get_currency_types():
    currency_types = [currency.value for currency in list(Currency_type)]
    return { "currency_types": currency_types }

@app.get('/convert')
async def convert(
    convert_from: Annotated[Currency_type, Query(description="The currency you will transfer from")],
    convert_to: Annotated[Currency_type, Query(description="The currency to which you will convert")],
    amount: Annotated[Decimal, Query(description="The financial amount you will transfer")]
):
    res = await get_currency_rates()
    currency = res.get("currency_rates")
    rate = currency.get(convert_from.value) / currency.get(convert_to.value)
    return { "converted_value": amount*rate }