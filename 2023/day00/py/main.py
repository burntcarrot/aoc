def part_a(input_path):
    return 0


def test_a():
    assert 0 == part_a('test_input.txt')


def part_b(input_path):
    return 0


def test_b():
    assert 0 == part_b('test_input.txt')


def read_input(input_path):
    with open(input_path, 'r') as file:
        data = file.readlines()

    return data


if __name__ == '__main__':
    test_a()
    print('Day 00a:', part_a('input.txt'))
    test_b()
    print('Day 00b:', part_b('input.txt'))