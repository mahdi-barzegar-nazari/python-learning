"""Exercise: distance from the origin to the point (3, 4).

Approach:
    Unpack the tuple into ``x`` and ``y``, then apply the Pythagorean theorem:
    distance = sqrt(x**2 + y**2). Raising to the power 0.5 is a square root.

Complexity:
    Time:  O(1) - a fixed number of arithmetic operations.
    Space: O(1).

Other ways:
    x = coordinates[0]; y = coordinates[1]   # indexing instead of unpacking
    math.hypot(x, y)                         # the standard-library shortcut

The result is a float (5.0) because ``**`` with 0.5 produces one.
"""

coordinates = (3, 4)

x, y = coordinates

distance = (x**2 + y**2) ** 0.5

print(distance)  # 5.0
