

# More on lists 
# The methods of the lists 
# Lsit comprehension 
# nested List comprehension 
# Techniques of looping 


"""
List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
"""


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

transpose = []

for i in range(4):
    transpose.append([row[i] for row in matrix])

print(transpose)
print('Hllow World')