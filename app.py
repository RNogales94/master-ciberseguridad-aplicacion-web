from flask import Flask, Response
import requests
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get-price/<ticker>")
def get_price(ticker):
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    response = requests.get(url)
    company_info = response.json()

    print(company_info)

    price = company_info['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
    company_name = company_info['quoteSummary']['result'][0]['price']['longName']
    exchange = company_info['quoteSummary']['result'][0]['price']['exchangeName']
    currency = company_info['quoteSummary']['result'][0]['price']['currency']

    result = {
        "price": price,
        "name": company_name,
        "exchange": exchange,
        "currency": currency
    }
    print(result)

    return Response(json.dumps(result))


if __name__ == '__main__':
    app.run()


