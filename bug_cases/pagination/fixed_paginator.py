"""
Fixed Paginator with boundary validation and metadata breakdown.
Refactored and tested using Cursor AI.
"""

from typing import Any, Dict, List
import math


def paginate(items: List[Any], page: int = 1, per_page: int = 10) -> Dict[str, Any]:
    """
    Safely paginates a list with strict boundary clamping and complete pagination metadata.
    """
    if per_page <= 0:
        raise ValueError(f"per_page must be greater than 0, got {per_page}")

    total_items = len(items)
    total_pages = max(1, math.ceil(total_items / per_page))
    
    # Clamp requested page between 1 and total_pages
    current_page = max(1, min(page, total_pages))

    start_idx = (current_page - 1) * per_page
    end_idx = min(start_idx + per_page, total_items)

    page_data = items[start_idx:end_idx]

    return {
        "data": page_data,
        "page": current_page,
        "per_page": per_page,
        "total_items": total_items,
        "total_pages": total_pages,
        "has_next": current_page < total_pages,
        "has_prev": current_page > 1
    }
