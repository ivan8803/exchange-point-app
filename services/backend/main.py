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

@app.get('/get_rates')
async def get_rates():
    req = requests.get("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt")
    currency = process_currency_req(req)
    return currency

@app.get('/convert_price_from_czk/{currency_type}')
async def convert_to_czk(
    currency_type: Annotated[Currency_type, Path(description="The currency you want to transfer money to")],
    price: Annotated[Decimal, Query(description="The amount of CZK you want to convert")]
    ):
    currency = await get_rates()
    rate = currency.get(currency_type.value)
    
    return price/rate

@app.get('/name_day')
async def get_nameday():
    req = requests.get("https://nameday.abalin.net/api/V1/today")
    data = json.loads(req.text)
    return data.get("nameday").get("cz")

@app.get('/currency_type')
async def get_currency_type():
    currency_types = [currency.value for currency in list(Currency_type)]
    return currency_types

@app.get('/convert')
async def convert(
    convert_from: Annotated[Currency_type, Query(description="The currency you will transfer from")],
    convert_to: Annotated[Currency_type, Query(description="The currency to which you will convert")],
    amount: Annotated[Decimal, Query(description="The financial amount you will transfer")]
):
    currency = await get_rates()
    rate = currency.get(convert_from.value) / currency.get(convert_to.value)
    return amount*rate