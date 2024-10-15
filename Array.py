#Write a Python program that performs the following operations using the numpy module:

# Create a 1D NumPy array from a list of integers provided by the user.
# Reshape the array into a 2D array (if possible) with 2 rows and print the result.
# Calculate and print the sum of all the elements in the array.
# Find and print the mean, median, and standard deviation of the array.
# Sort the array in ascending order and print the sorted array.
# Create a new array that contains only the even numbers from the original array and print it.
# Find and print the maximum and minimum values in the array.
# Multiply every element in the array by 2 and print the resulting array.
# Flatten the 2D array (if applicable) back into a 1D array and print it.
# Find the dot product of the original array with itself and print the result.


import numpy as np

# Function to perform all the array operations
def array_operations():
    # 1. Create a 1D NumPy array from a list of integers provided by the user
    user_input = input("Enter a list of integers separated by spaces: ")
    array_1d = np.array([int(x) for x in user_input.split()])
    print(f"1D Array: {array_1d}")

    # 2. Reshape the array into a 2D array (if possible) with 2 rows and print the result
    try:
        array_2d = array_1d.reshape(2, -1)
        print(f"Reshaped 2D Array (2 rows):\n{array_2d}")
    except ValueError:
        print("Cannot reshape array into 2 rows. Total number of elements is not even.")

    # 3. Calculate and print the sum of all the elements in the array
    array_sum = np.sum(array_1d)
    print(f"Sum of all elements: {array_sum}")

    # 4. Find and print the mean, median, and standard deviation of the array
    mean_value = np.mean(array_1d)
    median_value = np.median(array_1d)
    std_deviation = np.std(array_1d)
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Standard Deviation: {std_deviation}")

    # 5. Sort the array in ascending order and print the sorted array
    sorted_array = np.sort(array_1d)
    print(f"Sorted Array: {sorted_array}")

    # 6. Create a new array that contains only the even numbers from the original array and print it
    even_numbers = array_1d[array_1d % 2 == 0]
    print(f"Array with even numbers: {even_numbers}")

    # 7. Find and print the maximum and minimum values in the array
    max_value = np.max(array_1d)
    min_value = np.min(array_1d)
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")

    # 8. Multiply every element in the array by 2 and print the resulting array
    multiplied_array = array_1d * 2
    print(f"Array with elements multiplied by 2: {multiplied_array}")

    # 9. Flatten the 2D array (if applicable) back into a 1D array and print it
    if array_1d.size % 2 == 0:  # Only flatten if reshaped was successful
        flattened_array = array_2d.flatten()
        print(f"Flattened Array: {flattened_array}")
    else:
        print("Skipping flattening, reshaping was not possible.")

    # 10. Find the dot product of the original array with itself and print the result
    dot_product = np.dot(array_1d, array_1d)
    print(f"Dot product of the array with itself: {dot_product}")

# Call the function to execute
array_operations()


# Sample Input 
# Enter a list of integers separated by spaces: 1 2 3 4 5 6

# Sample Output:
#1D Array: [1 2 3 4 5 6]

# Reshaped 2D Array (2 rows):
# [[1 2 3]
#  [4 5 6]]

# Sum of all elements: 21

# Mean: 3.5
# Median: 3.5
# Standard Deviation: 1.707825127659933

# Sorted Array: [1 2 3 4 5 6]

# Array with even numbers: [2 4 6]

# Maximum value: 6
# Minimum value: 1

# Array with elements multiplied by 2: [ 2  4  6  8 10 12]

# Flattened Array: [1 2 3 4 5 6]

# Dot product of the array with itself: 91
