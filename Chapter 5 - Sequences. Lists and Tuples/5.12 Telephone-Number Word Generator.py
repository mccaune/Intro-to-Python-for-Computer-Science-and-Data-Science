"""
5.12
(Telephone-Number Word Generator) You should find this exercise to be entertaining. 
Standard telephone keypads contain the digits zero through nine. The numberstwo through 
nine each have three letters associated with them, as shown in the followingtable:

"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"

Many people find it difficult to memorize phone numbers, so they use the correspondence between 
digits and letters to develop seven-letter words (or phrases) that correspond to their phone numbers. 
For example, a person whose telephone number is 686-2377 might use the correspondence indicated 
in the preceding table to develop the sevenletter word “NUMBERS.” Every seven-letter word or phrase 
corresponds to exactly one seven-digit telephone number. A budding data science entrepreneur might 
like to reserve the phone number 244-3282 (“BIGDATA”). Every seven-digit phone number without 0s or 1s 
corresponds to many different seven-letter words, but most of these words represent unrecognizable gibberish. 
A veterinarian with the phone number 738-2273 would be pleased to know that the number corresponds to 
the letters “PETCARE.” Write a script that, given a seven-digit number, generates every possible seven-letter
word combination corresponding to that number. There are 2,187 (37) such combinations. 
Avoid phone numbers with the digits 0 and 1 (to which no letters correspond). 
See if your phone number corresponds to meaningful words.
"""

def telephoneNumber(digits):
    if digits == "":
        return []
    d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = [""]
    for digit in digits:
        temp = []
        for letter in d[digit]:
            for r in result:
                temp.append(r + letter)
        result = temp
    result.sort()
    for i in range(len(result)):
        print(i+1, result[i])
    return result

telephoneNumber("25495")