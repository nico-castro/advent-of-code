#!/usr/local/bin/python3


def place_dots(arr: [(int, int)], rows: int, cols: int) -> [[str]]:
    grid = [['.']*cols for _ in range(rows)]
    for c, r in arr:
        grid[r][c] = '#'
    return grid


def fold_x(grid: [[str]], x: int) -> [[str]]:
    folded = [['.']*x for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(x):
            if grid[row][x-1-col] == '#' or grid[row][x+1+col] == '#':
                folded[row][x-1-col] = '#'
    return folded


def fold_y(grid: [[str]], y: int) -> [[str]]:
    folded = [['.']*len(grid[0]) for _ in range(y)]
    for row in range(y):
        for col in range(len(grid[0])):
            if grid[y-1-row][col] == '#' or grid[y+1+row][col] == '#':
                folded[y-1-row][col] = '#'
    return folded


def main():
    arr = []
    folds = []
    max_x = 0
    max_y = 0
    with open('input.txt') as f:
        for line in f:
            if line == '\n':
                continue
            if not line.startswith('fold'):
                x, y = tuple(map(int, line.rstrip().split(',')))
                arr.append((x, y))
            else:
                f = line.rstrip().split(' ')[-1]
                axis, index = f.split('=')[0], int(f.split('=')[1])
                folds.append((axis, index))
                if axis == 'x' and index > max_x:
                    max_x = index
                if axis == 'y' and index > max_y:
                    max_y = index

    paper = place_dots(arr, max_y*2+1, max_x*2+1)

    for axis, index in folds:
        if axis == 'x':
            paper = fold_x(paper, int(index))
        else:
            paper = fold_y(paper, int(index))

    for row in paper:
        print(row)


if __name__ == "__main__":
    main()
