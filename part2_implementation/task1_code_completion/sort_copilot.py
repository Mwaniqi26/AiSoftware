
# sort_copilot.py

# GitHub Copilot suggested version
def sort_dicts(data, key):
    """
    Sorts a list of dictionaries by the given key, using .get() for safety.
    """
    return sorted(data, key=lambda d: d.get(key, ''))


# Example usage:
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob"},  # missing 'age'
    {"name": "Charlie", "age": 30}
]

sorted_people = sort_dicts(people, "age")
print(sorted_people)
