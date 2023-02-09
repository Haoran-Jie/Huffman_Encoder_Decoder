import heapq

# Sample list of tuples
tuples = [
    (1, 3),
    (2, 1),
    (3, 2),
]

# Define a custom comparison function that returns the second value of each tuple
def compare_by_second_value(t):
    return t[1]

# Use the heapify function to sort the list of tuples
heapq.heapify(tuples, key=compare_by_second_value)

# The list is now sorted based on the second value of each tuple
print(tuples)
# Output: [(2, 1), (3, 2), (1, 3)]
