def get_end_coordinates(directions):
    coordinates = [0, 0]
    for direction in directions:
        direction = direction.upper()
        if direction == 'N':
            coordinates[1] += 1
        elif direction == 'S':
            coordinates[1] -= 1
        elif direction == 'E':
            coordinates[0] += 1
        elif direction == 'W':
            coordinates[0] -= 1
    return coordinates

moves = []
while True:
    print('Enter N, S, E, or W (or blank to stop):')
    move = input()
    if move == '':
        break
    moves.append(move)

print(get_end_coordinates(moves))
