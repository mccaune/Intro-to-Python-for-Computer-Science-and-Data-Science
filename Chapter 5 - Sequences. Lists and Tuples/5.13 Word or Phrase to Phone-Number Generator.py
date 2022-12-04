"""
5.13
(Word or Phrase to Phone-Number Generator) Just as people would enjoy knowing what word or phrase their 
phone number corresponds to, they might choose a wordor phrase appropriate for their business and determine 
what phone numbers correspond to it. These are sometimes called vanity phone numbers, and various websites 
sell suchphone numbers. Write a script similar to the one in the previous exercise that produces the
possible phone number for the given seven-letter string.
"""

def numberCombinations(letters):
    if letters == "":
        return []
    d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = [""]
    for letter in letters:
        temp = []
        for digit in d:
            if letter in d[digit]:
                for r in result:
                    temp.append(r + digit)
        result = temp
    print(result)
    return result

numberCombinations("caterpillar")