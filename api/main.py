import requests
import json
import os
from dotenv import load_dotenv
from companies import companies

def get_data(companies: dict, daterange:int):


    load_dotenv()
    api_key = os.environ.get("api-token")

    symbol = "AAPL"
    interval = "1day" 
    outputSize = "3" # how many days it goes back


    # 1096 days needed for 3 years


    url = f"https://api.twelvedata.com/avgprice?symbol={symbol}&interval={interval}&outputsize={outputSize}&apikey={api_key}"

    # THIS WILL HAVE SOME MISSING DATA, FOR NON TRADING DAYS SUCH AS WEEKENDS AND BANK HOLIDAYS. 
    # HENCE, AUTOFILL THESE DATES WITH THE LAST DATA SET AVAILABLE

    data = requests.get(url).json()

    print(json.dumps(data, indent=4))


def main():
    get_data(companies, 3)

if __name__ == "__main__":
    main()