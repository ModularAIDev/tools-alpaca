import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient

load_dotenv()
api_key_id = os.getenv('API_KEY_ID')
secret_key = os.getenv('SECRET_KEY')

trading_client = TradingClient(api_key_id, secret_key)

__account = trading_client.get_account()
