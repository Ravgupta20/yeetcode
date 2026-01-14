"""
Palantir FDEE Interview Prep - BASICS
Pure Python Fundamentals (No Repetition)

This file introduces core Python concepts one at a time.
After completing this, move to easy.py for spaced repetition practice.
"""

# =============================================================================
# SECTION 1: LISTS
# =============================================================================

# Question 1: Create a list with numbers 1 through 5
numList=[1,2,3,4,5]

# Question 2: Create an empty list
emptyList = list()

# Question 3: Append an element to a list
numList.append(7)

# Question 4: Get the length of a list
# Hint: len()

# Question 5: Access first element (index 0)

# Question 6: Access last element (negative indexing)
# Hint: Use -1

# Question 7: Slice a list [start:end] **
# Given: nums = [0, 1, 2, 3, 4, 5]
# Get elements from index 2 to 4 (inclusive of 2, exclusive of 5)

# Question 8: Check if an element exists in a list **
# Hint: 3 in my_list

# Question 9: Get the index of an element **
# Hint: my_list.index(value)

# Question 10: Remove an element by value
# Hint: my_list.remove(value)
numList.remove(3)

# =============================================================================
# SECTION 2: DICTIONARIES
# =============================================================================

# Question 11: Create an empty dictionary


# Question 12: Create a dictionary with key-value pairs **
# Example: {'name': 'Alice', 'age': 25}
myDict = {'name': 'Alice', 'age': 25}

# Question 13: Add a new key-value pair to a dictionary **
myDict['city'] = 'NYC'

# Question 14: Access a value by key
# Hint: my_dict[key]


# Question 15: Use .get() to safely access a key that might not exist **
# Hint: my_dict.get('missing_key', default_value)
# myDict['Address']

# Question 16: Check if a key exists in a dictionary ***
# Hint: 'key' in my_dict

# Question 17: Delete a key from a dictionary
# Hint: del my_dict[key]
myDict['Address'] = "123 Main St"
del myDict['Address']


# Question 18: Get all keys as a list
# Hint: list(my_dict.keys())

# Question 19: Get all values as a list
# Hint: list(my_dict.values())


# Question 20: Get all key-value pairs as tuples
# Hint: list(my_dict.items())


# =============================================================================
# SECTION 3: SETS
# =============================================================================

# Question 21: Create a set from a list (removes duplicates)
# Given: nums = [1, 2, 2, 3, 3, 3]
# Hint: set(nums)


# Question 22: Create an empty set
# Hint: set() NOT {} (that's an empty dict)


# Question 23: Add an element to a set
# Hint: my_set.add(value)


# Question 24: Remove an element from a set
# Hint: my_set.remove(value)


# Question 25: Check if element exists in set
# Hint: value in my_set


# Question 26: Set intersection (common elements)
# Given: set1 = {1, 2, 3}, set2 = {2, 3, 4}
# Hint: set1 & set2 or set1.intersection(set2)


# Question 27: Set union (all unique elements)
# Hint: set1 | set2 or set1.union(set2)


# Question 28: Set difference (elements in set1 but not set2)
# Hint: set1 - set2 or set1.difference(set2)


# =============================================================================
# SECTION 4: TUPLES
# =============================================================================

# Question 29: Create a tuple
# Hint: my_tuple = (1, 2, 3)


# Question 30: Access tuple elements by index
# Hint: Same as lists: my_tuple[0]


# Question 31: Unpack a tuple into variables
# Given: point = (10, 20)
# Hint: x, y = point


# Question 32: Swap two variables using tuple unpacking
# Hint: a, b = b, a


# =============================================================================
# SECTION 5: STRINGS
# =============================================================================

# Question 33: Split a string into a list of words
# Given: text = "hello world python"
# Hint: text.split()


# Question 34: Join a list of strings with a separator
# Given: words = ['hello', 'world']
# Hint: ' '.join(words)


# Question 35: Check if a substring exists in a string
# Hint: 'sub' in 'substring'


# Question 36: Convert string to uppercase
# Hint: text.upper()


# Question 37: Convert string to lowercase
# Hint: text.lower()


# Question 38: Remove leading/trailing whitespace
# Hint: "  hello  ".strip()


# Question 39: Replace substring in a string
# Hint: text.replace('old', 'new')


# Question 40: Get string length
# Hint: len(text)


# =============================================================================
# SECTION 6: BASIC LOOPS
# =============================================================================

# Question 41: Loop through a list
# Given: nums = [1, 2, 3, 4, 5]
# Hint: for num in nums:


# Question 42: Loop with index using range
# Hint: for i in range(len(nums)):


# Question 43: Loop with enumerate (get both index and value)
# Hint: for i, val in enumerate(nums):


# Question 44: Loop through dictionary keys
# Hint: for key in my_dict: or for key in my_dict.keys():


# Question 45: Loop through dictionary values
# Hint: for value in my_dict.values():


# Question 46: Loop through dictionary key-value pairs
# Hint: for key, value in my_dict.items():


# =============================================================================
# SECTION 7: BASIC MATH & UTILITIES
# =============================================================================

# Question 47: Find maximum value in a list
# Hint: max(nums)


# Question 48: Find minimum value in a list
# Hint: min(nums)


# Question 49: Sum all numbers in a list
# Hint: sum(nums)


# Question 50: Get absolute value of a number
# Hint: abs(-5)


# Question 51: Round a float to N decimal places
# Hint: round(3.14159, 2)


# Question 52: Check if number is even using modulo
# Hint: num % 2 == 0


# Question 53: Integer division (floor division)
# Hint: 7 // 2 gives 3 (not 3.5)


# Question 54: Power/exponent
# Hint: 2**3 or pow(2, 3)


# Question 55: Create a range of numbers
# Hint: list(range(10)) creates [0, 1, 2, ..., 9]


# =============================================================================
# SECTION 8: CONDITIONALS & BASIC FUNCTIONS
# =============================================================================

# Question 56: Use any() to check if at least one element is True
# Given: nums = [1, 3, 5, 7]
# Check if any number > 5
# Hint: any(x > 5 for x in nums)


# Question 57: Use all() to check if all elements are True
# Check if all numbers are positive
# Hint: all(x > 0 for x in nums)


# Question 58: Ternary operator (conditional expression)
# Assign "even" if num is even, else "odd"
# Hint: result = "even" if num % 2 == 0 else "odd"


# =============================================================================
# CONGRATULATIONS!
# You've learned the pure fundamentals. Now you're ready for easy.py
# which will use spaced repetition to reinforce these concepts!
# =============================================================================
