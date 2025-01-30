def sort_string (strings):
    sorted_list = ["".join(sorted(s)) for s in strings]
    sorted_list.sort()
    return sorted_list


input_strings = ["Github", "Python", "Sorting", "Array"]
print(sort_string(input_strings))
