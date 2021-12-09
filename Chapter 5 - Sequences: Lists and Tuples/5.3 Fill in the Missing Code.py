"""
5.3 Fill in the Missing Code) Replace the ***s in the following list comprehension and
function call, such that given a list of heights in inches, the code maps the list to a list
of tuples containing the original height values and their corresponding values in meters.
For example, if one element in the original list contains the height 69 inches, the corre-
sponding element in the new list will contain the tuple (69, 1.7526), representing both
the height in inches and the height in meters. There are 0.0254 meters per inch.

[*** for x in [69, 77, 54]]
list(map(lambda ***, [69, 77, 54]))
"""

#5.3
a = [(x, x * 0.0254) for x in [69, 77, 54]]
print(a)
b = list(map(lambda x: (x, x * 0.0254), [69, 77, 54]))
print(b)
