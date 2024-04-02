from crewai_tools import tool
from config import __account as acc


@tool("returns Alpaca accountount restriction or not")
def check_if_account_restricted() -> bool:
    """Return if account is restricted or not."""
    return acc.trading_blocked


@tool("Get buying power on Alpaca (accountount purchasing power).")
def get_buying_power() -> str:
    """Returns a string with the number of dollars as the purchasing power of the accountount."""
    return f"{acc.buying_power}$"
