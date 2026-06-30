# This program gets a list of integers from the user and calculates the frequency of 
# each integer in the list. Also, it returns the numbers sorted by frequency from
# highest to lowest frequency. If two numbers have the same frequency, they are sorted in ascending order.
from collections import Counter
def get_integer_list() -> list[int]:
    while True:
        user_input = input("Enter a list of integers separated by comma: ")
        try:
            integer_list = [int(num) for num in user_input.split(",") if num.strip()]
            integer_list.sort()
            return integer_list
        except ValueError:
            print("Invalid input. Please enter only integers separated by comma.")
            
def main() -> None:
    integer_list = get_integer_list()
    frequency_map = Counter(integer_list)
    sorted_frequency_map = dict(sorted(frequency_map.items(), key=lambda item: (-item[1], item[0])))
    
    print("Frequency of each integer:")
    for num, freq in sorted_frequency_map.items():
        print(f"{num}: {freq}")
        
if __name__ == "__main__":
    main()