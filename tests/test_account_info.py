import unittest
import random
from unittest.mock import patch
from aic_tools_alpaca.account_info import CheckIfAccountRestricted
from aic_tools_alpaca.account_info import GetBuyingPower


class TestAccountFunctions(unittest.TestCase):
    @patch('aic_tools_alpaca.account_info.acc')
    def test_check_account_status_blocked(self, mock_acc):
        mock_acc.trading_blocked = True
        self.assertTrue(CheckIfAccountRestricted()._run())
    
    @patch('aic_tools_alpaca.account_info.acc')
    def test_check_account_status_not_blocked(self, mock_acc):
        mock_acc.trading_blocked = False
        self.assertFalse(CheckIfAccountRestricted()._run())
        
    @patch('aic_tools_alpaca.account_info.acc')
    def test_print_buying_power(self, mock_acc):
        random_buying_power = random.randint(10000, 200000)
        mock_acc.buying_power = random_buying_power
        self.assertEqual(GetBuyingPower()._run(), f"{random_buying_power}$")


if __name__ == '__main__':
    unittest.main()
