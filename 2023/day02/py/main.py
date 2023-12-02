def read_input(input_path):
    with open(input_path, 'r') as file:
        return file.read().splitlines()

def get_games(lines):
    games = []
    for line in lines:
        game_info = line.split(": ")[-1] # omit the "Game 1:" prefix
        rounds = [round_info.split(', ') for round_info in game_info.split('; ')] # split into sets/rounds
        games.append(rounds)
    
    return games

def is_game_possible(game_info, cube_counts):
    for subset in game_info:
        # get color and count info
        # example: {'red': 15, 'green': 16, 'blue': 3}
        subset_counts = {color: int(count.split()[0]) for count, color in (item.split() for item in subset)}
        
        for color, count in subset_counts.items():
            if cube_counts.get(color, 0) < count:
                return False
    
    return True

def part_a(input_path):
    lines = read_input(input_path)
    games = get_games(lines)
    
    target_cube_counts = {'red': 12, 'green': 13, 'blue': 14}
    possible_games_ids = []
    
    for i, game in enumerate(games):
        if is_game_possible(game, target_cube_counts):
            possible_games_ids.append(i + 1) # remember that we need to calculate the sum of game IDs

    return sum(possible_games_ids)

def test_a():
    return 8 == part_a('test_input.txt')

def part_b(input_path):
    lines = read_input(input_path)
    games = get_games(lines)

    ans = 0
    for game in games:
        # get subsets for colors and calculate max
        # similar logic like Part A
        red = max(int(count.split()[0]) for subset in game for count, color in (item.split() for item in subset) if "red" in color)
        green = max(int(count.split()[0]) for subset in game for count, color in (item.split() for item in subset) if "green" in color)
        blue = max(int(count.split()[0]) for subset in game for count, color in (item.split() for item in subset) if "blue" in color)
        
        # Power = multiply max of R, G, B
        ans += red * green * blue
    
    return ans

def test_b():
    return 2286 == part_b('test_input2.txt')

if __name__ == '__main__':
    print("Test 1:", test_a())
    print('Day 02a:', part_a('input.txt'))
    print("Test 2:", test_b())
    print('Day 02b:', part_b('input.txt'))