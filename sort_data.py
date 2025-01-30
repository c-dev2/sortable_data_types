from sort_int import sort_int
from merge_array import merge_arrays
from sort_doubles import sort_doubles
from Sort_String import sort_string

print("Type 1 to sort integers.")
print("Type 2 to merge arrays of integers.")
print("Type 3 to sort doubles.")
print("Type 4 to sort the letters in a string.")

user_input = int(input("Please enter in your selection: "))

while user_input not in [1, 2, 3, 4]:
    user_input = int(input("Please only enter in one of the above numbers: "))

match user_input:
    case 1:
        user_array = input("Enter in your list of integers separated by a space: ").split()
        user_array_int = list(map(int, user_array))
        print(sort_int(user_array_int))

    case 2:
        print("Enter integers separated by spaces:")
        array1 = list(map(int, input("Please enter the first unsorted array: ").split()))
        array2 = list(map(int, input("Please enter the second unsorted array: ").split()))
        merged_array = merge_arrays(array1, array2)
        print("Merged and sorted array:", merged_array)

    case 3:
        user_array = input("Enter in your list of doubles separated by a space: ").split()
        user_array_doubles = list(map(float, user_array))
        print(sort_doubles(user_array_doubles))

    case 4:
        user_array = input("Enter in your string: ")
        print("".join(sort_string(user_array)))
