"""
5.5 (IPython Session: Slicing) Create a string called alphabet containing 'abcdefghijklmnopqrstuvwxyz' then perform the following separate slice operations to obtain:
a) The first half of the string using starting and ending indices.
b) The first half of the string using only the ending index.
c) The second half of the string using starting and ending indices.
d) The second half of the string using only the starting index.
e) Every second letter in the string starting with 'a'.
f) The entire string in reverse.
g) Every third letter of the string in reverse starting with 'z'.
"""


#5.5
alphabet = 'abcdefghijklmnopqrstuvwxyz'
a = alphabet[0:int(len(alphabet)/2)]
print(a)
b = alphabet[:int(len(alphabet)/2)]
print(b)
c = alphabet[int(len(alphabet)/2):len(alphabet)]
print(c)
d = alphabet[int(len(alphabet)/2):]
print(d)
e = alphabet[0:len(alphabet):2]
print(e)
f = alphabet[::-1]
print(f)
g = alphabet[-1:0:-3]
print(g)
