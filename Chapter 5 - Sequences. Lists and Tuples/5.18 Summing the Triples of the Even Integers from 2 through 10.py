"""
5.18
(Summing the Triples of the Even Integers from 2 through 10) Starting with a list
containing 1 through 10, use filter, map and sum to calculate the total of the triples of
the even integers from 2 through 10. Reimplement your code with list comprehensions
rather than filter and map.
"""

numbers_1 = list(range(1, 11))

# Filter out only even numbers
even_numbers_1 = list(filter(lambda x: x % 2 == 0, numbers_1))
# Map each even number to its triple
triples_of_evens_1 = list(map(lambda x: x * 3, even_numbers_1))
# Compute the total sum
total_1 = sum(triples_of_evens_1)

print(f'solution 1 (filter, map): {total_1}')


numbers_2 = list(range(1, 11))

# List comprehension to select only even numbers
even_numbers_2 = [x for x in numbers_2 if x % 2 == 0]
# List comprehension to triple each even number
triples_of_evens_2 = [x * 3 for x in even_numbers_2]
# Compute the total sum
total_2 = sum(triples_of_evens_2)

print(f'solution 2 (list comprehensions): {total_2}')