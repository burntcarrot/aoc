import re

def ways_to_beat_record(times, distances):
    total_ways = 1

    for time, distance in zip(times, distances):
        ways = 0
        for hold_time in range(time + 1):
            boat_speed = hold_time
            remaining_time = time - hold_time
            total_distance = boat_speed * remaining_time
            if total_distance > distance:
                ways += 1

        total_ways *= ways

    return total_ways

def ways_to_beat_record_single_race(total_time, record_distance):
    ways = 0

    for hold_time in range(1, total_time):
        boat_speed = hold_time
        remaining_time = total_time - hold_time
        total_distance = boat_speed * remaining_time
        if total_distance > record_distance:
            ways += 1

    return ways

def part_a(input_path):
    with open(input_path, 'r') as file:
        lines = file.read().splitlines()

    time_line = re.sub(r'\D', ' ', lines[0])
    times = list(map(int, time_line.split()))

    distance_line = re.sub(r'\D', ' ', lines[1])
    distances = list(map(int, distance_line.split()))

    result = ways_to_beat_record(times, distances)
    return result

def part_b(input_path):
    with open(input_path, 'r') as file:
        lines = file.read().splitlines()

    total_time = int(re.sub(r'\D', '', lines[0]))
    record_distance = int(re.sub(r'\D', '', lines[1]))

    result_single_race = ways_to_beat_record_single_race(total_time, record_distance)
    return result_single_race

def test_a():
    return part_a('test_input.txt') == 288

def test_b():
    return part_b('test_input2.txt') == 71503

if __name__ == '__main__':
    print("Test 1:", test_a())
    print('Day 06a:', part_a('input.txt'))
    print("Test 2:", test_b())
    print('Day 06b:', part_b('input.txt'))
