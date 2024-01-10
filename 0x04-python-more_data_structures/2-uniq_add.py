#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Convert the list to a set to remove duplicates
    unique_set = set(my_list)

    # Sum all the values in the set
    total = sum(unique_set)

    return total
