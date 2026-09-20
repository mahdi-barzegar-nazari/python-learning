"""Exercise: split a sentence into lowercase words.

Approach:
    ``str.lower()`` returns a new lowercase string, and ``str.split()`` with
    no argument cuts on any run of whitespace. Chaining them does both steps
    in one line.

Complexity (n = number of characters):
    Time:  O(n) - lower() and split() each scan the string once.
    Space: O(n) - a new string and a list of words are created.

The same thing in two steps, which is easier to debug:
    lowered = sentence.lower()
    words = lowered.split()
"""

sentence = "Hi this is a string"
print(sentence.lower().split())  # ['hi', 'this', 'is', 'a', 'string']
