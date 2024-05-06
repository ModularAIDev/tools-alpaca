import unittest
import random
from unittest.mock import patch, MagicMock

from aic_tools_alpaca import TradingClientSingleton
from aic_tools_alpaca.account_info import (
    CheckIfTradingBlocked, GetTotalBuyingPower,
    GetNonMarginableBuyingPower, GetAccountEquity,
)


class TestAccountFunctions(unittest.TestCase):
    def setUp(self):
        self.mock_trading_client = MagicMock()
        self.mock_account = MagicMock()
        TradingClientSingleton.get_instance = MagicMock(return_value=self.mock_trading_client)
        self.mock_trading_client.get_account.return_value = self.mock_account

    def _test_account_buying_powers(self, account_info_class, test_attribute_name):
        random_value = random.randint(0, 999999)
        setattr(self.mock_account, test_attribute_name, random_value)
        self.assertEqual(account_info_class()._run(), f"{random_value}$")

    def test_check_trading_blocked_true(self):
        setattr(self.mock_account, 'trading_blocked', True)
        self.assertTrue(CheckIfTradingBlocked()._run())

    def test_check_trading_not_blocked_false(self):
        setattr(self.mock_account, 'trading_blocked', False)
        self.assertFalse(CheckIfTradingBlocked()._run())

    def test_total_buying_power(self):
        self._test_account_buying_powers(GetTotalBuyingPower, 'buying_power')

    def test_non_margin_buying_power(self):
        self._test_account_buying_powers(GetNonMarginableBuyingPower, 'non_marginable_buying_power')

    def test_account_equity(self):
        self._test_account_buying_powers(GetAccountEquity, 'equity')


if __name__ == '__main__':
    unittest.main()
