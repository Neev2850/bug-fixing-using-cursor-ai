"""
Safe Deep Dictionary & JSON Navigation.
Fix suggested by Cursor AI with fallback defaults and keypath traversal.
"""

from typing import Any, Dict, List, Optional


def safe_get(data: Any, *keys: str, default: Any = None) -> Any:
    """
    Safely traverses nested dictionaries/iterables using variadic key arguments.
    Returns `default` if any key is missing or encounters a NoneType.
    """
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
        else:
            return default

        if current is None:
            return default

    return current


def extract_user_city(api_response: Optional[Dict[str, Any]]) -> str:
    """Safely extracts city or returns 'Unknown City'."""
    city = safe_get(api_response, "data", "user", "profile", "address", "city", default="Unknown City")
    return str(city).strip()
