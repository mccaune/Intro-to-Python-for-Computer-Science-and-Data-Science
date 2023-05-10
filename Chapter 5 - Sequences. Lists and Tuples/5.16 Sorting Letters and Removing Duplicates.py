"""
5.16
(Sorting Letters and Removing Duplicates) Insert 20 random letters in the range
'a' through 'f' into a list. Perform the following tasks and display your results:
a) Sort the list in ascending order.
b) Sort the list in descending order.
c) Get the unique values sort them in ascending order.
"""

import random
import string

# Initialize an empty list to store the random letters
letters = []

# Use a for loop to generate 20 random letters from the range 'a' through 'f'
for _ in range(20):
    # Get a random letter from the first 6 lowercase letters ('a' through 'f')
    random_letter = random.choice(string.ascii_lowercase[:6])
    
    # Append the random letter to the list
    letters.append(random_letter)

# a) Sort the list in ascending order
ascending = sorted(letters)

# b) Sort the list in descending order
descending = sorted(letters, reverse=True)

# c) Get the unique values and sort them in ascending order
unique_ascending = sorted(set(letters))

# Display the results
print(f"Original list: {letters}")
print(f"Ascending order: {ascending}")
print(f"Descending order: {descending}")
print(f"Unique values in ascending order: {unique_ascending}")