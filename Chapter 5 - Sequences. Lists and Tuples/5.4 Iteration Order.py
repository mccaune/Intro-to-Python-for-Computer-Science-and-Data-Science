"""
5.4 (Iteration Order) Create a 2-by-3 list, then use a nested loop to:
a) Set each element’s value to an integer indicating the order in which it was pro-
cessed by the nested loop.
b) Display the elements in tabular format. Use the column i
"""


#5.4

#a
lst = [[11, 12, 13], [14, 15, 16]]
count = 1
for i, row in enumerate(lst):
    for j, item in enumerate(row):
        lst[i][j] =  count
        count += 1
print(lst)


#b
lst1 = [[11, 12, 13], [14, 15, 16]]
indent = 3+ len(str(len(lst1)))
print('     ', end='')
for col in range(len(lst1[0])):
    print(f'{col:>{col}}', end=' ')
print()
for i, row in enumerate(lst1):
    print(f'{i} -', end=' ')
    for j, item in enumerate(row):
        print(item, end=' ')
    print('')
