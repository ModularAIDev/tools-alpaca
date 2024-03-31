import unittest
from tools_alp.some_time import get_time


class TestGetTime(unittest.TestCase):
    def test_get_time_known_timezone(self):
        # Check real time zone
        self.assertNotEqual(get_time("Europe/Kyiv"), "Unknown timezone")

    def test_unknown_timezone(self):
        # Check invalid timezone
        result = get_time("Not/A_Timezone")
        self.assertEqual(result, "Unknown timezone")


if __name__ == "__main__":
    unittest.main()
