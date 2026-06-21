def is_palindrome(text):
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


def main():
    print("This program checks if a string is a palindrome.")
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print(f"{input_string} is a palindrome.")
    else:
        print(f"{input_string} is not a palindrome.")


if __name__ == "__main__":
    main()
