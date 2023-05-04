"""
5.14
(Is a Sequence Sorted?) Create a function is_ordered that receives a sequence 
and returns True if the elements are in sorted order. 
Test your function with sorted and un-sorted lists, tuples and strings.
"""
def is_ordered(sequence):
    for i, element in enumerate(sequence[:-1]):
        # Compare the current element with the next element
        if element > sequence[i + 1]:
            # If the current element is greater than the next element, return False
            return False
        
        # If all elements are in sorted order, return True
        return True


# Test with sorted and unsorted lists
sorted_list = [1, 2, 3, 4, 5]
unsorted_list = [5, 2, 1, 4, 3]

print(is_ordered(sorted_list))     # True
print(is_ordered(unsorted_list))   # False

# Test with sorted and unsorted tuples
sorted_tuple = (1, 2, 3, 4, 5)
unsorted_tuple = (5, 2, 1, 4, 3)

print(is_ordered(sorted_tuple))    # True
print(is_ordered(unsorted_tuple))  # False

# Test with sorted and unsorted strings
sorted_string = "abcdef"
unsorted_string = "fedcba"

print(is_ordered(sorted_string))   # True
print(is_ordered(unsorted_string)) # False