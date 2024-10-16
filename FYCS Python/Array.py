#Write a Python program that performs the following operations using the numpy module:

# Create a 1D NumPy array from a list of integers provided by the user.
# Calculate and print the sum of all the elements in the array.
# Sort the array in ascending order and print the sorted array.
# Find and print the maximum and minimum values in the array.


import numpy as np

# Function to perform all the array operations
def array_operations():
    # 1. Create a 1D NumPy array from a list of integers provided by the user
    user_input = input("Enter a list of integers separated by spaces: ")
    array_1d = np.array([int(x) for x in user_input.split()])
    print(f"1D Array: {array_1d}")

    # 2. Calculate and print the sum of all the elements in the array
    array_sum = np.sum(array_1d)
    print(f"Sum of all elements: {array_sum}")

    # 3. Sort the array in ascending order and print the sorted array
    sorted_array = np.sort(array_1d)
    print(f"Sorted Array: {sorted_array}")

    # 4. Find and print the maximum and minimum values in the array
    max_value = np.max(array_1d)
    min_value = np.min(array_1d)
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")


# Call the function to execute
array_operations()


# Sample Input 
# Enter a list of integers separated by spaces: 1 2 3 4 5 6

# Sample Output:
#1D Array: [1 2 3 4 5 6]

# Sum of all elements: 21

# Sorted Array: [1 2 3 4 5 6]

# Maximum value: 6
# Minimum value: 1

