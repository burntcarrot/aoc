def return_sets(card_str):
    winning, current = card_str.split('|')
    winning = set(winning.split(':')[1].strip().split(' ')) # yep, a bunch of string parsing
    winning.discard('') # remove empty
    current = set(current.strip().split(' '))
    return winning, current

def part_a(input_path):
    lines = read_input(input_path)
    total = 0
    for line in lines:
        winning, current = return_sets(line)
        num_matches = len(winning & current) # set intersection to find total number of matching card numbers
        total += 2 ** (num_matches - 1) if num_matches > 0 else 0
    return total

def part_b(input_path):
    lines = read_input(input_path)
    card_counts = [1] * len(lines)

    for i, line in enumerate(lines, 1):
        winning, current = return_sets(line)
        for j in range(len(winning & current)):
            card_counts[i + j] += card_counts[i - 1]
    return sum(card_counts)

def test_a():
    return part_a('test_input.txt') == 13

def test_b():
    return part_b('test_input2.txt') == 30

def read_input(input_path):
    with open(input_path, 'r') as file:
        data = file.readlines()

    return data

if __name__ == '__main__':
    print("Test 1:", test_a())
    print('Day 04a:', part_a('input.txt'))
    print("Test 2:", test_b())
    print('Day 04b:', part_b('input.txt'))
