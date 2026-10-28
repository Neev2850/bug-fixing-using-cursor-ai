# Bug Scenario 1: Mutable Default Argument Trap
# Root Cause: Default arguments in Python are evaluated once when the function is defined,
# not each time the function is called.

class ShoppingBasket:
    def __init__(self, owner: str, items: list = []):  # BUG: mutable default argument
        self.owner = owner
        self.items = items

    def add_item(self, item: str):
        self.items.append(item)
        return self.items
