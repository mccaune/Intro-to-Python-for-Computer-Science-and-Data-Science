"""
5.19
(Finding the People with a Specified Last Name) Create a list of tuples containing
first and last names. Use filter to locate the tuples containing the last name Jones. 
Ensure that several tuples in your list have that last name.
"""

# List of tuples containing first and last names
names_list = [
    ('John', 'Smith'),
    ('Jane', 'Doe'),
    ('Michael', 'Jones'),
    ('Sarah', 'Jones'),
    ('David', 'Williams'),
    ('Emily', 'Jones')
]

# Use filter to locate tuples containing the last name 'Jones'
jones_last_names = list(filter(lambda name: name[1] == 'Jones', names_list))

# Display the tuples with last name 'Jones'
print("Tuples with last name 'Jones':")
for first, last in jones_last_names:
    print(f"{first} {last}")