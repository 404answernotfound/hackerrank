def formingMagicSquare(s):
    s = sum(s, []) 
    magic_squares = [
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
    ]
    costs = []
    for magic_square in magic_squares:
        costs.append(sum([abs(magic_square[i] - s[i]) for i in range(9)]))

    return min(costs) 
