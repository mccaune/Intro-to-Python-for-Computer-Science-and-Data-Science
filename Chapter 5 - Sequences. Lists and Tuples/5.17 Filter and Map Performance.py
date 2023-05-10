"""
5.17
(Filter/Map Performance) With regard to the following code:

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
list(map(lambda x: x ** 2,
filter(lambda x: x % 2 != 0, numbers)))

a) How many times does the filter operation call its lambda argument?
b) How many times does the map operation call its lambda argument?
c) If you reverse the filter and map operations, how many times does the map op-
eration call its lambda argument?

To help you answer the preceding questions, define functions that perform the same tasks
as the lambdas. In each function, include a print statement so you can see each time the
function is called. Finally, replace the lambdas in the preceding code with the names of
your functions.
"""

def is_odd(x):
    print(f"Filter called with {x}")
    return x % 2 != 0

def square(x):
    print(f"Map called with {x}")
    return x ** 2

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

# a) How many times does the filter operation call its lambda argument?
# b) How many times does the map operation call its lambda argument?
result = list(map(square, filter(is_odd, numbers)))
print(f"Result: {result}")

# c) If you reverse the filter and map operations,
# how many times does the map operation call its lambda argument?
result_reversed = list(filter(is_odd, map(square, numbers)))
print(f"Result with reversed operations: {result_reversed}")


"""
Based on the output, we can answer the questions:

a) The filter operation calls its lambda argument (is_odd function) 10 times, once for each number in the list.

b) The map operation calls its lambda argument (square function) 5 times, once for each odd number after filtering.

c) If we reverse the filter and map operations, the map operation (square function) will be called 10 times, once for each number in the list.
"""