import os

from crewai_tools import BaseTool

from dotenv import load_dotenv
from alpaca.trading.client import TradingClient

load_dotenv()
api_key_id = os.getenv('API_KEY_ID')
secret_key = os.getenv('SECRET_KEY')

trading_client = TradingClient(api_key_id, secret_key)
acc = trading_client.get_account()


class CheckIfAccountRestricted(BaseTool):
    name: str = "Accountant restriction status."
    description: str = "Return if account is restricted or not."

    def _run(self) -> bool:
        # Your tool's logic here
        return acc.trading_blocked


class GetBuyingPower(BaseTool):
    name: str = "Accountant purchasing power."
    description: str = "Returns a string with the number of dollars as the purchasing power of the accountant."

    def _run(self) -> str:
        # Your tool's logic here
        return f"{acc.buying_power}$"

