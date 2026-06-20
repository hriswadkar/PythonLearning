# First Program


def build_table(number, limit=10):
    return [f"{number} x {i} = {number * i}" for i in range(1, limit + 1)]


def main():
    print("Table of 2")
    for line in build_table(2):
        print(line)


if __name__ == "__main__":
    main()
