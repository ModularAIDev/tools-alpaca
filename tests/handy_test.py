import os
from aic_tools_alpaca.account_info import (
    CheckIfTradingBlocked, GetNonMarginableBuyingPower, GetTotalBuyingPower, GetAccountEquity
)

print(f"Is trading prohibited: {CheckIfTradingBlocked()._run()}")
print(f"Accountant total purchasing power is: {GetTotalBuyingPower()._run()}")
print(f"Accountant purchasing power without margin is: {GetNonMarginableBuyingPower()._run()}")
print(f"Total equinty is: {GetAccountEquity()._run()}")


def clear_env(keys):
    """Remove specified ENVs."""
    for key in keys:
        os.environ.pop(key, None)  # is pop safety removing?
        print(f"ENV removed for '{key}': {key not in os.environ}")


keys_to_clear = ['API_KEY_ID', 'SECRET_KEY']
clear_env(keys_to_clear)
