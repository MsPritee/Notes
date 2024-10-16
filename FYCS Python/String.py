# Write a Python program that takes a sentence as input from the user and performs the following operations on the string:

# Convert the entire string to uppercase and print it.
# Convert the entire string to lowercase and print it.
# Replace all spaces with underscores (_) and print the new string.
# Count and print the number of vowels (a, e, i, o, u) in the string.
# Reverse the string and print the result.
# Find and print the index of the first occurrence of the letter a. If it does not exist, print -1.
# Slice and print the first 5 characters of the string.



# Function to perform all the string operations
def string_operations():
    # Take input from the user
    user_input = input("Enter a sentence: ")

    # 1. Convert the entire string to uppercase
    upper_case = user_input.upper()
    print(f"Uppercase: {upper_case}")

    # 2. Convert the entire string to lowercase
    lower_case = user_input.lower()
    print(f"Lowercase: {lower_case}")

    # 3. Replace all spaces with underscores
    replaced_string = user_input.replace(' ', '_')
    print(f"Replaced spaces with underscores: {replaced_string}")

    # 4. Count the number of vowels in the string
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in user_input if char in vowels)
    print(f"Number of vowels: {vowel_count}")

    # 5. Reverse the string
    reversed_string = user_input[::-1]
    print(f"Reversed string: {reversed_string}")

    # 6. Find the index of the first occurrence of 'a'
    first_a_index = user_input.find('a')
    if first_a_index != -1:
        print(f"Index of first 'a': {first_a_index}")
    else:
        print("No 'a' found in the string.")

    # 7. Slice and print the first 5 characters
    first_five_chars = user_input[:5]
    print(f"First 5 characters: {first_five_chars}")

# Call the function to execute
string_operations()


# Sample Input:
# Enter a sentence: I love My INDIA.


# Uppercase: I LOVE MY INDIA.
# Lowercase: i love my india.
# Replaced spaces with underscores: I_love_My_INDIA.
# Number of vowels: 6
# Reversed string: .AIDNI yM evol I
# Index of first 'a': 14
# First 5 characters: I lov









