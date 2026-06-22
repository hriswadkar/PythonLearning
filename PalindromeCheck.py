# This program checks if a given string is a palindrome or not.

def reverse_string(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Reverse the string using slicing
    return s[::-1]

def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

def main():
    # Prompt the user for input
    user_input = input("Enter a string to check if it's a palindrome: ")
    reversed_str = reverse_string(user_input)
    is_pal = is_palindrome(user_input)
    print(f'Reversed: "{reversed_str}"')
    print(f'Is Palindrome: {is_pal}')

if __name__ == "__main__":
    main()