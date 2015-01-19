import unittest

from flask.ext.responses import utility


class TestUtility(unittest.TestCase):
    def test_set_headers(self):
        from flask import Response
        res = Response()
        self.assertEqual(res.headers.get("foo", ""), "")

        res = utility.set_headers(res, {"foo": "bar"})
        self.assertEqual(res.headers.get("foo", ""), "bar")
