"""
Diagnostics Runner: Demonstrating Logic Flaws & Cursor AI Fixes
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from bug_cases.mutable_default.buggy_cart import ShoppingBasket as BuggyBasket
from bug_cases.mutable_default.fixed_cart import ShoppingBasket as FixedBasket

from bug_cases.pagination.buggy_paginator import paginate_buggy
from bug_cases.pagination.fixed_paginator import paginate as paginate_fixed

from bug_cases.json_parser.buggy_parser import extract_user_city_buggy
from bug_cases.json_parser.fixed_parser import extract_user_city, safe_get


def demo_mutable_default():
    print("\n--- 1. Mutable Default Argument Trap ---")
    print("Testing Buggy Implementation (shared list state):")
    b1 = BuggyBasket("Alice")
    b1.add_item("Mechanical Keyboard")
    print(f"Alice's items: {b1.items}")

    b2 = BuggyBasket("Bob")
    print(f"Bob's items before adding anything: {b2.items} <-- BUG: Contains Alice's item!")

    print("\nTesting Fixed Implementation:")
    fb1 = FixedBasket("Alice")
    fb1.add_item("Mechanical Keyboard")
    print(f"Alice's items: {fb1.get_items()}")

    fb2 = FixedBasket("Bob")
    print(f"Bob's items before adding anything: {fb2.get_items()} <-- FIXED: Clean isolated list!")


def demo_pagination():
    print("\n--- 2. Off-By-One In Pagination ---")
    data = ["Doc0", "Doc1", "Doc2", "Doc3", "Doc4", "Doc5", "Doc6", "Doc7"]
    print(f"Original dataset (8 items): {data}")

    buggy_page1 = paginate_buggy(data, page=1, per_page=3)
    print(f"Buggy Page 1 (per_page=3): {buggy_page1} <-- BUG: Doc0 skipped due to 1-based indexing!")

    fixed_page1 = paginate_fixed(data, page=1, per_page=3)
    print(f"Fixed Page 1 (per_page=3): {fixed_page1['data']} <-- FIXED: Doc0 included correctly!")


def demo_json():
    print("\n--- 3. Unsafe Deep JSON Access ---")
    broken_payload = {"data": {"user": {"profile": None}}}
    print(f"Payload with missing intermediate address: {broken_payload}")

    try:
        extract_user_city_buggy(broken_payload)
    except TypeError as e:
        print(f"Buggy parser crashed with: TypeError - {e}")

    fixed_city = extract_user_city(broken_payload)
    print(f"Fixed parser handled safely, returning fallback: '{fixed_city}'")


if __name__ == "__main__":
    print("=" * 60)
    print("    CURSOR AI DEBUGGING & ROOT CAUSE RESOLUTION SUITE")
    print("=" * 60)
    demo_mutable_default()
    demo_pagination()
    demo_json()
    print("\nAll diagnostics completed successfully.")
