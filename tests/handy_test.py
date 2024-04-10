from aic_tools_alpaca.account_info import CheckIfAccountRestricted
from aic_tools_alpaca.account_info import GetBuyingPower


status = CheckIfAccountRestricted()._run()


print("Is restricted: ")
print(status)

buying_power_message = GetBuyingPower()._run()
print("Current purchasing power: ")
print(buying_power_message)
