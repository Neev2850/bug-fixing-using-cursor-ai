# Bug Scenario 2: Off-By-One In Pagination
# Causes: Assuming 1-indexed math for list slicing or missing edge cases on boundary divisions.

def paginate_buggy(items: list, page: int, per_page: int):
    # Bug: Off-by-one in start slice and unbounded end slice
    start = (page - 1) * per_page + 1  # BUG: skips the 0th item!
    end = page * per_page
    return items[start:end]
