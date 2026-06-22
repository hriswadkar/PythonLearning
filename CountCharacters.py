# This program counts how many times each character appears in a given string.

def count_characters(input_string):
    character_count = {}
    
    for char in input_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
            
    return character_count

def main():
    """Prompt the user for a string and display the character count."""
    print("This program counts how many times each character appears in a string.")
    input_string = input("Enter a string: ")
    character_count = count_characters(input_string)
    for char, count in character_count.items():
        print(f"'{char}': {count}")


if __name__ == "__main__":
    main()