#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element with another in a new list.

    Args:
        my_list: The initial list.
        search: The element to replace.
        replace: The new element.

    Returns:
        A new list with all occurrences of `search` replaced with `replace`.
    """

    new_list = []
    for item in my_list:
        new_list.append(replace if item == search else item)  # Concise conditional logic
    return new_list
