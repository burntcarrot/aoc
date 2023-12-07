from collections import Counter
from functools import cmp_to_key

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def calculate_hand_type(hand):
    counter = Counter(hand)
    counts = counter.most_common()

    if counts[0][1] == 5:
        return 7
    elif counts[0][1] == 4:
        return 6
    elif counts[0][1] == 3 and counts[1][1] == 2:
        return 5
    elif counts[0][1] == 3:
        return 4
    elif counts[0][1] == 2 and counts[1][1] == 2:
        return 3
    elif counts[0][1] == 2:
        return 2

    return 1

def compare_hands(h1, h2, ordering):
    t1 = calculate_hand_type(h1[0])
    t2 = calculate_hand_type(h2[0])

    if t1 != t2:
        return -1 if t1 < t2 else 1

    for card_h1, card_h2 in zip(h1[0], h2[0]):
        if ordering[card_h1] < ordering[card_h2]:
            return -1
        elif ordering[card_h1] > ordering[card_h2]:
            return 1

    return 0

def calculate_score(hands):
    ans = 0
    for i, hand in enumerate(hands):
        ans += (i + 1) * hand[1]
    return ans

def part_a(input_path):
    lines = read_input(input_path)
    hands = [(line.split()[0], int(line.split()[1])) for line in lines]
    hands.sort(key=cmp_to_key(lambda h1, h2: compare_hands(h1, h2, ORDERING)))

    return calculate_score(hands)

def test_a():
    return 6440 == part_a('test_input.txt')

def calculate_hand_type_b(hand):
    counter = Counter(hand)
    j_count = counter['J']
    del counter['J']
    counts = counter.most_common()

    if len(counts) <= 1:
        return 7
    if counts[0][1] + j_count == 5:
        return 7
    elif (counts[0][1] + j_count == 4) or (counts[0][1] == 4 and j_count == 1):
        return 6
    elif (counts[0][1] + j_count == 3 and counts[1][1] == 2) or (counts[0][1] == 3 and counts[1][1] + j_count == 2):
        return 5
    elif counts[0][1] + j_count == 3:
        return 4
    elif (counts[0][1] + j_count == 2 and counts[1][1] == 2) or (counts[0][1] == 2 and counts[1][1] + j_count == 2):
        return 3
    elif counts[0][1] + j_count == 2:
        return 2

    return 1

def compare_hands_b(h1, h2):
    t1 = calculate_hand_type_b(h1[0])
    t2 = calculate_hand_type_b(h2[0])

    if t1 != t2:
        return -1 if t1 < t2 else 1

    for card_h1, card_h2 in zip(h1[0], h2[0]):
        if ORDERING_B[card_h1] < ORDERING_B[card_h2]:
            return -1
        elif ORDERING_B[card_h1] > ORDERING_B[card_h2]:
            return 1

    return 0

def part_b(input_path):
    lines = read_input(input_path)
    hands = [(line.split()[0], int(line.split()[1])) for line in lines]
    hands.sort(key=cmp_to_key(compare_hands_b))

    return calculate_score(hands)

def test_b():
    return 5905 == part_b('test_input2.txt')

if __name__ == '__main__':
    ORDERING = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
    ORDERING_B = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}
    print("Test 1:", test_a())
    print('Day 07a:', part_a('input.txt'))
    print("Test 2:", test_b())
    print('Day 07b:', part_b('input.txt'))