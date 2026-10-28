"""
Fixed ShoppingBasket using None sentinel pattern.
Identified and resolved via Cursor AI assistance.
"""

from typing import List, Optional


class ShoppingBasket:
    def __init__(self, owner: str, items: Optional[List[str]] = None):
        """
        Uses None as default value and creates a fresh list instance per object,
        preventing unexpected cross-instance memory sharing.
        """
        self.owner = owner
        self.items: List[str] = list(items) if items is not None else []

    def add_item(self, item: str) -> List[str]:
        if not item or not item.strip():
            raise ValueError("Item name cannot be empty")
        self.items.append(item.strip())
        return self.items

    def get_items(self) -> List[str]:
        return list(self.items) # Return defensive copy
