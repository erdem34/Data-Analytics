import unittest

from visuanalytics.tests.analytics.transform.transform_test_helper import prepare_test


class TestTransformLowerCase(unittest.TestCase):
    def setUp(self):
        self.data = {
            "test": ["canada", "CANADA", "CaNaDa", "cAnAdA", "Canada"]
        }

    def test_lower_case(self):
        values = [
            {
                "type": "lower_case",
                "keys": ["_req|test"],
                "new_keys": ["_req|test1"]
            }
        ]

        expected_data = {
            "_req": {
                "test": ["canada", "CANADA", "CaNaDa", "cAnAdA", "Canada"],
                "test1": ["canada", "canada", "canada", "canada", "canada"]
            }
        }

        exp, out = prepare_test(values, self.data, expected_data)
        self.assertDictEqual(exp, out, "lower case failed")
