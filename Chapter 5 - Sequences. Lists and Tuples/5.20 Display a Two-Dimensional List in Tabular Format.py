"""
5.20
Define a function named
display_table that receives a two-dimensional list and displays its contents in tabular for-
mat. List the column indices as headings across the top, and list the row indices at the left
of each row.
"""

def display_table(data):
    num_rows = len(data)
    num_cols = len(data[0]) if num_rows > 0 else 0

    # Display column indices as headings
    col_indices = ["   "] + [f"{i:<4}" for i in range(num_cols)]
    col_line = "+".join(["-" * len(col) for col in col_indices])
    print(" ".join(col_indices))
    print(col_line)

    # Display data with row indices
    for i, row in enumerate(data):
        row_str = [f"{i:<2} |"]
        for item in row:
            row_str.append(f"{item:<4}")
        print(" ".join(row_str))

# Example two-dimensional list
data = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
]

# Call the display_table function with the example data
display_table(data)

