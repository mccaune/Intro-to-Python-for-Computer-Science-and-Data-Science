"""
5.15
(Tuples Representing Invoices) When you purchase products or services from a
company, you typically receive an invoice listing what you purchased and the total amount
of money due. Use tuples to represent hardware store invoices that consist of four pieces
of data—a part ID string, a part description string, an integer quantity of the item being
purchased and, for simplicity, a float item price (in general, Decimal should be used for
monetary amounts). Use the sample hardware data shown in the following table.

Part number	Part description	Quantity	Price
83	    Electric sander	        7	        57.98
24	    Power saw	            18	        99.99
7	    Sledge hammer	        11	        21.5
77	    Hammer	                76	        11.99
39	    Jig saw	                3           79.5

Perform the following tasks on a list of invoice tuples:
a) Use function sorted with a key argument to sort the tuples by part description,
then display the results. To specify the element of the tuple that should be used
for sorting, first import the itemgetter function from the operator module as in
from operator import itemgetter
Then, for sorted’s key argument specify itemgetter(index) where index
specifies which element of the tuple should be used for sorting purposes.
b) Use the sorted function with a key argument to sort the tuples by price, then
display the results.
c) Map each invoice tuple to a tuple containing the part description and quantity,
sort the results by quantity, then display the results.
d) Map each invoice tuple to a tuple containing the part description and the value
of the invoice (the product of the quantity and the item price), sort the results
by the invoice value, then display the results.
e) Modify Part (d) to filter the results to invoice values in the range $200 to $500.
f) Calculate the total of all the invoices.
"""
from operator import itemgetter

# Sample hardware data
invoices = [
    ('83', 'Electric sander', 7, 57.98),
    ('24', 'Power saw', 18, 99.99),
    ('7', 'Sledge hammer', 11, 21.5),
    ('77', 'Hammer', 76, 11.99),
    ('39', 'Jig saw', 3, 79.5)
]

# a) Sort the tuples by part description
sorted_by_description = sorted(invoices, key=itemgetter(1))
print("Sorted by part description:")
for invoice in sorted_by_description:
    print(invoice)


# b) Sort the tuples by price
sorted_by_price = sorted(invoices, key=itemgetter(3))
print("\nSorted by price:")
for invoice in sorted_by_price:
    print(invoice)


# c) Sort the tuples by quantity
# Map each invoice tuple to a tuple containing the part description and quantity
result_c = [(t[1], t[2]) for t in invoices]

# Sort the results by quantity
result_c_sorted = sorted(result_c, key=lambda t: t[1])

# Display the results
print("\nSorted by quantity:")
for part, qty in result_c_sorted:
    print(f"{part:15} {qty}")


# d) Sort the tuples by invoice value
# Map each invoice tuple to a tuple containing the part description and the value of the invoice
result_d = [(t[1], t[2]*t[3]) for t in invoices]

# Sort the results by the invoice value
result_d_sorted = sorted(result_d, key=lambda t: t[1])

# Display the results
print("\nSorted by invoice value:")
for part, value in result_d_sorted:
    print(f"{part:15} ${value:.2f}")


# e) Filter the results to invoice values in the range $200 to $500
# Filter the results to invoice values in the range $200 to $500
result_e_filtered = list(filter(lambda t: 200 <= t[1] <= 500, result_d))
sorted_filtered_invoices = sorted(result_e_filtered, key=lambda x: x[1])

print("\nSorted by invoice value (in the range $200 to $500):")
for invoice in sorted_filtered_invoices:
    print(f'{invoice[0]:20} {invoice[1]:>8.2f}')

# f) Calculate the total of all the invoices
total = sum(qty * price for (_, _, qty, price) in invoices)
print("\nTotal of all the invoices:", total)


