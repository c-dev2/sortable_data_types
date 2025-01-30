def sort_int(arr):
    for i in arr:
        if type(i) is not int:
            return -1

    sorted_arr = sorted(arr)
    return sorted_arr