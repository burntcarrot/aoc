"""
featuring my "functional" spaghetti code
"""

import re


def found_symbol(lines, row, start, end):
    # Check if there is any non-digit, non-dot character in a specified range of a given row.
    new_start = max(0, start - 1)
    return any(
        re.search(r'[^.\d]', lines[r][new_start:end + 1])
        for r in range(row - 1, row + 2)
        if 0 <= r < len(lines)
    )


def find_star_chars(lines, stars, row, start, end, part_num):
    # Find '*' characters in a specified range of a given row and record their positions.
    new_start = max(0, start - 1)
    stars.update(
        ((r, new_start + match.start(0)), stars.get((r, new_start + match.start(0)), []) + [part_num])
        for r in range(row - 1, row + 2)
        if 0 <= r < len(lines)
        for match in [re.search(r'\*', lines[r][new_start:end + 1])]
        if match
    )


def part_a(input_path):
    lines = read_input(input_path)

    # Calculate sum of part numbers.
    return sum(
        int(match[0])
        for i, line in enumerate(lines)
        for match in re.finditer('\d+', line)
        if found_symbol(lines, i, match.start(), match.end())
    )


def part_b(input_path):
    lines = read_input(input_path)
    stars = {}
    
    for i, line in enumerate(lines):
        for match in re.finditer('\d+', line): # match '\d+' (one or more digits) in the line.
            part_num = int(match[0])
            # Find '*' characters and record their positions.
            find_star_chars(lines, stars, i, match.start(), match.end(), part_num)

    # Calculate ratios.
    return sum(part_nums[0] * part_nums[1]
               for star_pos, part_nums in stars.items()
               if len(part_nums) == 2)


def test_a():
    return part_a('test_input.txt') == 4361


def test_b():
    return part_b('test_input2.txt') == 467835


def read_input(input_path):
    with open(input_path) as input_file:
        return input_file.read().strip().split('\n')


if __name__ == '__main__':
    print("Test 1:", test_a())
    print('Day 03a:', part_a('input.txt'))
    print("Test 2:", test_b())
    print('Day 03b:', part_b('input.txt'))
