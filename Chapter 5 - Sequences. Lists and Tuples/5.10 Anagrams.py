"""
5.10
(Anagrams) An anagram of a string is another string formed by rearranging the let-
ters in the first. Write a script that produces all possible anagrams of a given string using
only techniques that you’ve seen to this point in the book. [The itertools module pro-
vides many functions, including one that produces permutations.]
"""

def anagram(s):
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        stack.append(s[i])
        for j in range(len(stack)):
            stack.append(stack[j] + s[i])
            stack[j] = s[i] + stack[j]
    print(stack)


anagram("abc")
