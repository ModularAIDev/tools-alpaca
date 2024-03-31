import unittest
import random
from unittest.mock import patch, Mock
from tools_alp.account_info import _check_account_status_logic, _print_buying_power_logic


class TestAccountFunctions(unittest.TestCase):
    @patch('tools_alp.account_info.acc')
    def test_check_account_status_blocked(self, mock_acc):
        mock_acc.trading_blocked = True
        self.assertEqual(_check_account_status_logic(), 'Account is currently restricted from trading.')
    
    @patch('tools_alp.account_info.acc')
    def test_check_account_status_not_blocked(self, mock_acc):
        mock_acc.trading_blocked = False
        self.assertIsNone(_check_account_status_logic(), None)
        
    @patch('tools_alp.account_info.acc')
    def test_print_buying_power(self, mock_acc):
        random_buying_power = random.randint(10000, 200000)
        mock_acc.buying_power = random_buying_power
        self.assertEqual(_print_buying_power_logic(), f'{random_buying_power}$ is available as buying power.')


if __name__ == '__main__':
    unittest.main()
