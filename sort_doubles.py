
def sort_doubles(double_values):

    for value in double_values:
        if type(value) is not float:
            return -1
        
    sorted_doubles = sorted(double_values)
    
    return sorted_doubles