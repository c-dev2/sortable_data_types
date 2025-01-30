from sort_int import sort_int

print("Type 1 to sort integers.")

user_input = int(input("Please enter in your selection: "))

while user_input not in [1, 2, 3, 4]:
    user_input = int(input("Please only enter in one of the above numbers: "))

match user_input:
    case 1:
        user_array = input("Enter in your list of integers separated by a space: ").split()
        user_array_int = list(map(int, user_array))
        print(sort_int(user_array_int))
