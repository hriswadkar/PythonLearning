# Count vowels in a string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

def main():
    print("This program checks if a string contains vowels.")
    input_string = input("Enter a string: ")
    vowel_count = count_vowels(input_string)
    print(f"The string contains {vowel_count} vowel(s).")


if __name__ == "__main__":
    main()