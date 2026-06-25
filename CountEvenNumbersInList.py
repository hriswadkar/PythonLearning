# This program accepts a list of numbers from the user and counts how many of them are even.
def count_even_numbers(numbers):
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    return even_count

def main():
    print("This program counts how many even numbers are in a list.")
    input_numbers = input("Enter a list of numbers separated by comma: ")
    number_list = [int(num) for num in input_numbers.split(",")]
    even_count = count_even_numbers(number_list)
    print(f"The list contains {even_count} even number(s).")

if __name__ == "__main__":
    main()