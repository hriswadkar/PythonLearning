# Count vowels in a string

VOWELS = frozenset("aeiouAEIOU")

def count_vowels(input_string):
    """Count and return the number of vowels in the given string.

    Args:
        input_string (str): The string to check for vowels.

    Returns:
        int: The number of vowel characters found.

    Raises:
        TypeError: If input_string is None.
    """
    if input_string is None:
        raise TypeError("input_string must be a string, not None")
    return sum(1 for char in input_string if char in VOWELS)

def main():
    """Prompt the user for a string and display the vowel count."""
    print("This program checks if a string contains vowels.")
    input_string = input("Enter a string: ")
    vowel_count = count_vowels(input_string)
    print(f"The string contains {vowel_count} vowel(s).")


if __name__ == "__main__":
    main()