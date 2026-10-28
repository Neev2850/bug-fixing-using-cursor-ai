# Bug Scenario 3: Unsafe Deep JSON Navigation
# Causes KeyError or TypeError: 'NoneType' object is not subscriptable

def extract_user_city_buggy(api_response: dict):
    # Crashes immediately if any intermediate key is None or missing
    return api_response["data"]["user"]["profile"]["address"]["city"]
