"""
5.7 (Duplicate Elimination) Create a function that receives a list and returns a (possi-
bly shorter) list containing only the unique values in sorted order. Test your function with
a list of numbers and a list of strings.
"""


#5.7
def duplicate_removal(data):
    lst = []
    for i in data:
        if i not in lst:
            lst.append(i)
    lst.sort()
    print(lst)
    return lst

duplicate_removal([3,3,3,4,5,6,7,8,9,5,4,3,3,35,2,22,1,2,3,23,23])
duplicate_removal(['a','a','a','a','d','dsg','g','g','g','sd','rt','wr','wqr','w','wr','wr','qw','rwr','w','s','s','a',])
