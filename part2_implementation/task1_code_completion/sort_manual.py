def sort_dicts(lst, key):
    """
    Sorts a list of dictionaries by the given key.
    """
    return sorted(lst, key=lambda x: x[key])

# Example usage:
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

sorted_people = sort_dicts(people, "age")
print(sorted_people)

