import unittest

from flask.ext.responses import utility


class TestUtility(unittest.TestCase):
    def test_set_headers(self):
        test_case = {}
        self.assertEqual(test_case.get("foo", ""), "")

        test_case = utility.set_headers(test_case, {"foo": "bar"})
        self.assertEqual(test_case.get("foo", ""), "bar")
