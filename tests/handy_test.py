from config import trading_client as client
from tools_alp.account_info import _check_account_status_logic, _print_buying_power_logic

account = client.get_account()

# Тепер ви можете використовувати цей об'єкт акаунта з вашими функціями
status = _check_account_status_logic()
buying_power_message = _print_buying_power_logic()

print(status)
print(buying_power_message)
