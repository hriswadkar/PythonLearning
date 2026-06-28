# This program accepts numbers from the user and 
# stores them in a list, then calculates and displays the 
# sum and average of the numbers.

input_list = []

def parse_input(input_string):
    return [int(x) for x in input_string.split(',') if x.strip().isdigit()]


def calculate_sum(input_list):
    total_sum = 0
    for num in input_list:
        total_sum += num
    return total_sum

def calculate_average(input_list):
    if len(input_list) == 0:
        return 0
    total_sum = calculate_sum(input_list)
    average = total_sum / len(input_list)
    return average

def find_largest(input_list):
    if len(input_list) == 0:
        return None
    largest = input_list[0]
    for num in input_list:
        if num > largest:
            largest = num
    return largest

def find_smallest(input_list):
    if len(input_list) == 0:
        return None
    smallest = input_list[0]
    for num in input_list:
        if num < smallest:
            smallest = num
    return smallest

def main():
    """Prompt the user for a list of numbers separated by commas and display 
    the sum, average, largest, and smallest numbers."""
    print("Enter numbers separated by commas.")
    input_string = input("Enter numbers: ")
    input_list = parse_input(input_string)
    total_sum = calculate_sum(input_list)
    print(f"Sum: {total_sum}")
    average = calculate_average(input_list)
    print(f"Average: {average}")
    largest = find_largest(input_list)
    print(f"Largest: {largest}")
    smallest = find_smallest(input_list)
    print(f"Smallest: {smallest}")

if __name__ == "__main__":
    main()