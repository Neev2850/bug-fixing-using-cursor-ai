import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import unittest
from bug_cases.mutable_default.fixed_cart import ShoppingBasket
from bug_cases.pagination.fixed_paginator import paginate
from bug_cases.json_parser.fixed_parser import extract_user_city, safe_get


class TestFixedBugs(unittest.TestCase):
    def test_basket_isolation(self):
        b1 = ShoppingBasket("User1")
        b1.add_item("Laptop")
        b2 = ShoppingBasket("User2")
        self.assertEqual(len(b2.get_items()), 0)
        self.assertEqual(len(b1.get_items()), 1)

    def test_pagination_bounds(self):
        items = list(range(10)) # 0 to 9
        res = paginate(items, page=1, per_page=4)
        self.assertEqual(res["data"], [0, 1, 2, 3])
        self.assertEqual(res["total_pages"], 3)
        self.assertTrue(res["has_next"])

        res_last = paginate(items, page=3, per_page=4)
        self.assertEqual(res_last["data"], [8, 9])
        self.assertFalse(res_last["has_next"])

    def test_safe_json_traversal(self):
        # Empty payload
        self.assertEqual(extract_user_city({}), "Unknown City")
        # None payload
        self.assertEqual(extract_user_city(None), "Unknown City")
        # Valid payload
        valid = {"data": {"user": {"profile": {"address": {"city": "Jaipur"}}}}}
        self.assertEqual(extract_user_city(valid), "Jaipur")


if __name__ == "__main__":
    unittest.main()
