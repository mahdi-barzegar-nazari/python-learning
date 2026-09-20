"""Exercise: remove the number 3 from a list, then append 10.

Approach:
    ``remove(3)`` deletes the first item whose value is 3, and ``append(10)``
    adds to the end.

Complexity (n = len(my_list)):
    Time:  O(n) - remove() scans for the value and shifts later items left;
           append() is amortized O(1).
    Space: O(1) extra - the list is changed in place.

Other ways to get the same result:
    my_list.pop(2)           # removes by INDEX; also O(n) because of the shift
    del my_list[2]           # removes by index; same cost as pop(2)
    my_list = my_list[:2] + my_list[3:] + [10]
                             # builds a new list: O(n) time and O(n) space

Note: remove() works on a value and raises ValueError if it is missing;
pop() and del work on a position and raise IndexError if it is out of range.
Here they agree only because 3 happens to sit at index 2.
"""

my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
my_list.append(10)
print(my_list)  # [1, 2, 4, 5, 10]
