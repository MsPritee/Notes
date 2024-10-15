# Write a Python program that takes a sentence as input from the user and performs the following operations on the string:

# Convert the entire string to uppercase and print it.
# Convert the entire string to lowercase and print it.
# Replace all spaces with underscores (_) and print the new string.
# Count and print the number of vowels (a, e, i, o, u) in the string.
# Reverse the string and print the result.
# Check if the string is a palindrome (a word or phrase that reads the same forwards and backwards) and print True or False.
# Split the string into individual words and print them as a list.
# Join the list of words back into a single string with hyphens (-) between each word and print it.
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

    # 6. Check if the string is a palindrome
    is_palindrome = user_input == reversed_string
    print(f"Is palindrome: {is_palindrome}")

    # 7. Split the string into individual words
    word_list = user_input.split()
    print(f"List of words: {word_list}")

    # 8. Join the list of words back into a string with hyphens
    hyphen_joined = '-'.join(word_list)
    print(f"Hyphen-joined string: {hyphen_joined}")

    # 9. Find the index of the first occurrence of 'a'
    first_a_index = user_input.find('a')
    if first_a_index != -1:
        print(f"Index of first 'a': {first_a_index}")
    else:
        print("No 'a' found in the string.")

    # 10. Slice and print the first 5 characters
    first_five_chars = user_input[:5]
    print(f"First 5 characters: {first_five_chars}")

# Call the function to execute
string_operations()


# Sample Input:
# Enter a sentence: A man a plan a canal Panama


# Uppercase: A MAN A PLAN A CANAL PANAMA
# Lowercase: a man a plan a canal panama
# Replaced spaces with underscores: A_man_a_plan_a_canal_Panama
# Number of vowels: 10
# Reversed string: amanaP lanac a nalp a nam A
# Is palindrome: False
# List of words: ['A', 'man', 'a', 'plan', 'a', 'canal', 'Panama']
# Hyphen-joined string: A-man-a-plan-a-canal-Panama
# Index of first 'a': 3
# First 5 characters: A man









