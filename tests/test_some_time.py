import unittest
from tools_alp.some_time import _get_time_logic


class TestGetTime(unittest.TestCase):
    def test_get_time_known_timezone(self):
        # Check real time zone
        self.assertNotEqual(_get_time_logic("Europe/Kyiv"), "Unknown timezone")

    def test_unknown_timezone(self):
        # Check invalid timezone
        result = _get_time_logic("Not/A_Timezone")
        self.assertEqual(result, "Unknown timezone")


if __name__ == "__main__":
    unittest.main()
