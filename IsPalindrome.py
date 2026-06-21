def normalize_text(text):
    """Return a lowercase alphanumeric-only version of the input text."""
    return "".join(char.lower() for char in text if char.isalnum())


def is_palindrome(text):
    """Return True when the input text reads the same forwards and backwards."""
    cleaned_text = normalize_text(text)
    return cleaned_text == cleaned_text[::-1]


def main():
    """Run the interactive palindrome checker."""
    print("This program checks if a string is a palindrome.")
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print(f"{input_string} is a palindrome.")
    else:
        print(f"{input_string} is not a palindrome.")


if __name__ == "__main__":
    main()
