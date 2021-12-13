#!/usr/local/bin/python3


def place_dots(arr: [(int, int)], rows: int, cols: int) -> [[int]]:
    grid = [[0]*cols for _ in range(rows)]
    for c, r in arr:
        grid[r][c] = 1
    return grid


def fold_x(grid: [[int]], x: int) -> [[int]]:
    folded = [[0]*x for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(x):
            if grid[row][x-1-col] or grid[row][x+1+col]:
                folded[row][x-1-col] = 1
    return folded


def fold_y(grid: [[int]], y: int) -> [[int]]:
    folded = [[0]*len(grid[0]) for _ in range(y)]
    for row in range(y):
        for col in range(len(grid[0])):
            if grid[y-1-row][col] or grid[y+1+row][col]:
                folded[y-1-row][col] = 1
    return folded


def main():
    arr = []
    folds = []
    r_max = 0
    c_max = 0
    with open('input.txt') as f:
        for line in f:
            if line == '\n':
                continue
            if not line.startswith('fold'):
                x, y = tuple(map(int, line.rstrip().split(',')))
                arr.append((x, y))
                if y > r_max:
                    r_max = y
                if x > c_max:
                    c_max = x
            else:
                folds.append(line.rstrip().split(' ')[-1])

    paper = place_dots(arr, r_max+1, c_max+1)

    for fold in folds:
        axis, index = fold.split('=')
        if axis == 'x':
            paper = fold_x(paper, int(index))
        else:
            paper = fold_y(paper, int(index))
        break

    tot = 0
    for row in paper:
        for col in row:
            if col == 1:
                tot += 1
    print(tot)


if __name__ == "__main__":
    main()
