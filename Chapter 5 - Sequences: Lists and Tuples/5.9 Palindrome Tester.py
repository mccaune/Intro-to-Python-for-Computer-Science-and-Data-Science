"""
(Palindrome Tester) A string that’s spelled identically backward and forward, like 'radar' is a palindrome. Write a function is_palindrome that takes a string and returns True if it’s a palindrome and False otherwise. Use a stack (simulated with a list as we did in Section 5.11) to help determine whether a string is a palindrome. Your function should ignore case sensitivity (that is, 'a' and 'A' are the same), spaces and punctuation.
"""


#5.9
def is_paliandrome(x):
    stack = []
    if x == x[::-1]:
        stack.append(x)
    print(stack)
    


is_paliandrome('abba')
is_paliandrome('asdf')
