"""
4.13 (Arbitrary Argument List) Calculate the product of a series of integers that are
passed to the function product, which receives an arbitrary argument list. Test your func-
tion with several calls, each with a different number of arguments.
"""

#4.13
def product(*args):
    product = 1
    for i in args:
        product *= i
    print(product)

product(2,2,2,2,2)
product(2)
product(2,2)

