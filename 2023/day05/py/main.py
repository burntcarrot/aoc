import re

def extract_numbers(s):
    return [int(x) for x in re.findall(r'(-?\d+).?', s)]

def parse_mapping(lines):
    return [extract_numbers(s) for s in lines[1:] if s]

def lookup_destination(mapping, index):
    for destination, start, length in mapping:
        if start <= index < start + length:
            return destination + (index - start)
    return index

def get_break_points(mapping):
    # Extract the start and end points from each mapping
    start_points = {start - 1 for dest, start, length in mapping}
    end_points = {start + length - 1 for dest, start, length in mapping}
    
    # Combine start and end points, and sort them to get break points
    return sorted(start_points | end_points)

def break_seed_range(low, high, breaks):
    ranges = []
    
    # Iterate through break points to split the seed range
    for break_point in breaks:
        if low < break_point < high:
            ranges.append((low, break_point))
            low = break_point + 1

    # If there's still a remaining range, add it to the result
    if low < high:
        ranges.append((low, high))
    
    return ranges

def parse_input(file_path):
    with open(file_path) as file:
        data = [x.rstrip('\n').split('\n') for x in file.read().split('\n\n')]

    seeds = extract_numbers(data[0][0])
    maps = [parse_mapping(lines) for lines in data[1:]]

    return seeds, maps

def apply_mapping_to_ranges(ranges, mapping):
    transformed_ranges = []
    
    # Get break points in the mapping
    break_points = get_break_points(mapping)
    
    # Break seed ranges based on break points
    for low, high in ranges:
        transformed_ranges.extend(break_seed_range(low, high, break_points))
    
    # Apply the mapping to the seed ranges
    return [(lookup_destination(mapping, x), lookup_destination(mapping, y)) for x, y in transformed_ranges]

def part_a(input_path):
    seeds, maps = parse_input(input_path)

    seed_numbers = []
    for seed in seeds:
        for mapping in maps:
            number = seed # temp storage
            seed = lookup_destination(mapping, seed) # update seed value
            if "test" in input_path:
                print(f"Seed {number} -> Transformed Seed: {seed} using Mapping: {mapping}")
        seed_numbers.append(seed)

    ans = min(seed_numbers)
    return ans

def part_b(input_path):
    seeds, maps = parse_input(input_path)

    # Create seed ranges from pairs of seed numbers
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    seed_numbers = []
    for seed_range in seed_ranges:
        ranges = [seed_range]
        for mapping in maps:
            if "test" in input_path:
                print(f"Mapping: {mapping}, Break Points: {get_break_points(mapping)}")
            
            # Apply mapping to the seed ranges
            ranges = apply_mapping_to_ranges(ranges, mapping)
            
            if "test" in input_path:
                print(f"Seed Range: {ranges} using Mapping: {mapping}")
        seed_numbers.extend(ranges)

    ans = min(x for x, _ in seed_numbers)
    return ans

def test_a():
    return part_a('test_input.txt') == 35

def test_b():
    return part_b('test_input2.txt') == 46

if __name__ == '__main__':
    print("Test 1:", test_a())
    print('Day 05b:', part_a('input.txt'))
    print("Test 2:", test_b())
    print('Day 05b:', part_b('input.txt'))
