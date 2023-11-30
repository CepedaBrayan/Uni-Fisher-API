import unittest

from .setup import client
from .test_cases import TEST_CASES


class TestMain(unittest.TestCase):
    def test_main(self):
        for test_case in TEST_CASES:
            _r = client.post("/event/", json=test_case)
            self.assertEqual(_r.status_code, 200)
