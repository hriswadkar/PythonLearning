def is_even(number):
    return number % 2 == 0


def main():
    print("This program checks if a number is even or odd.")
    input_number = int(input("Enter a number: "))
    if is_even(input_number):
        print(f"{input_number} is an even number.")
    else:
        print(f"{input_number} is an odd number.")


if __name__ == "__main__":
    main()