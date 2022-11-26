"""
5.11
(Summarizing Letters in a String) Write a function summarize_letters that receives a string 
and returns a list of tuples containing the unique letters and their frequencies in the string. 
Test your function and display each letter with its frequency. Your function should ignore case 
sensitivity (that is, 'a' and 'A' are the same) and ignore spaces and punctuation. 
When done, write a statement that says whether the string has all the letters of the alphabet.
"""

import string
def summarize_letters(s):

    d = {}

    s = s.translate(str.maketrans('', '', string.digits))  
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.lower()

    words = s.split()
    for word in words:
        for letter in word:
            d[letter] = d.get(letter, 0) + 1

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print (d)
    if len(d) == 26:
        print("String contains all alphabet letters")
    else:
        print("String does not contain all alphabet letters")


summarize_letters("The quick brown fox jumps over the lazy dog")
summarize_letters("The qui")