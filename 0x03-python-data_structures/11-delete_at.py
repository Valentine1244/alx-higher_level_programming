#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Create a new list to store the result
    result = []

    # Iterate over the elements in the original list
    for i in range(len(my_list)):
        # Skip the element at the specified index
        if i == idx:
            continue
        result.append(my_list[i])

    # Return the new list without the element at the specified index
    return result
