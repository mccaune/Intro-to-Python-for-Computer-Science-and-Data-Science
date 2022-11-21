"""
5.6 (Functions Returning Tuples) Define a function rotate that receives three argu-
ments and returns a tuple in which the first argument is at index 1, the second argument
is at index 2 and the third argument is at index 0. Define variables a, b and c containing
'Doug', 22 and 1984. Then call the function three times. For each call, unpack its result
into a, b and c, then display their values.
"""


#5.6
def rotate(one, two, three):
    result = (three, one, two)
    print(result)
    #print(type(result))
    return (result)


a = 'Doug'
b = 22
c = 1984
rotate(a, b, c)
