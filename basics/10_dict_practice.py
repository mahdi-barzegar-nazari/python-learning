"""Exercise: raise the banana price to 1100 and remove the apple.

Approach:
    Assigning to an existing key replaces its value; ``pop(key)`` removes the
    key and returns its value.

Complexity:
    Time:  O(1) on average for the assignment and for pop() (hash lookups).
    Space: O(1) extra.

Other ways to remove a key:
    del fruit_prices["apple"]      # same effect, but does not return the value
    fruit_prices.pop("apple", None)  # never raises if the key is missing

Note: pop("apple") and del both raise KeyError when the key does not exist.
"""

fruit_prices = {
    "apple": 1500,
    "banana": 1000,
    "orange": 1200,
}

fruit_prices["banana"] = 1100
fruit_prices.pop("apple")

print(fruit_prices)  # {'banana': 1100, 'orange': 1200}
