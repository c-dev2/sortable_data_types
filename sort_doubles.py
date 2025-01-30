
def sort_doubles(double_values):

    for value in double_values:
        if type(value) is not float:
            return -1
        
    sorted_doubles = sorted(double_values)
    
    return sorted_doubles


double_values = [88.7, 44.5, 66.89, 33.55, 99.0]

print((sort_doubles(double_values)))