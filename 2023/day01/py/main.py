def part_a(input_path):
    lines = read_input(input_path)

    total_sum = 0
    for line in lines:
        # Find the first digit, using next to fetch first "true" element from our iteration
        first_digit = next(char for char in line if char.isdigit())
        # Find the last digit, but we reverse the line.
        last_digit = next(char for char in reversed(line) if char.isdigit())
        total_sum += int(f"{first_digit}{last_digit}")

    return total_sum

def test_a():
    return 142 == part_a('test_input.txt')

def part_b(input_path):
    numbers = {
        "one": 1,
        "two": 2,
        'three': 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    lines = read_input(input_path)
    total_sum = 0

    # Idea is to iterate sequentially, and use our mapping to
    # append the real integer values to a temporary list
    # This helps in overcoming the challenge in handling both strings and integers

    # We add the first and last digits, and return total sum as we did in Part A

    for line in lines:
        digits = []
        # Using enumerate to get (index, character) pairs
        for idx, char in enumerate(line):
            if char.isdigit():
                digits.append(int(char))
            for number, value in numbers.items():
                if line.startswith(number, idx):
                    digits.append(value)
        
        total_sum += int(f"{digits[0]}{digits[-1]}")

    return total_sum

def test_b():
    return 281 == part_b('test_input2.txt')

def read_input(input_path):
    with open(input_path, 'r') as file:
        data = file.readlines()

    return data


if __name__ == '__main__':
    print("Test 1:", test_a())
    print('Day 01a:', part_a('input.txt'))
    print("Test 2:", test_b())
    print('Day 01b:', part_b('input.txt'))
