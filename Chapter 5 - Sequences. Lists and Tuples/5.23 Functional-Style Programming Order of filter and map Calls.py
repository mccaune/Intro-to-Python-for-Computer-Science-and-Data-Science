"""
5.23
(Functional-Style Programming: Order of filter and map Calls) When combining 
filter and map operations, the order in which they’re performed matters. Consider a
list numbers containing 10, 3, 7, 1, 9, 4, 2, 8, 5, 6 and the following code:

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)

Reorder this code to call map first and filter second. What happens and why?
"""

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
result = list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers)))
print(result)

#Explanation:
"""
In the original code, map is applied to the filtered numbers that are even. 
So, each even number is doubled. 
This is why you get [20, 8, 4, 16, 12] as the output.

In the reordered code, map is applied first, doubling all the numbers in the list. 
Then, filter is applied to select only the doubled even numbers. 
This is why you get [20, 14, 8, 4, 16, 12] as the output.
"""