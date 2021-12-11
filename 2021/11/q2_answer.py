#!/usr/local/bin/python3
def flash(r, c, grid, flashed):
    if flashed.get((r, c), None):
        return

    flashed[(r, c)] = 1

    neighbors = [(r-1, c-1), (r-1, c), (r-1, c+1),
                 (r, c-1), (r, c+1),
                 (r+1, c-1), (r+1, c), (r+1, c+1)]

    for x, y in neighbors:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            grid[x][y] += 1
            if grid[x][y] > 9:
                flash(x, y,  grid, flashed)


def step(grid: [[int]]) -> int:
    flashed = {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1
            if grid[r][c] > 9:
                flash(r, c, grid, flashed)
    for r, c in flashed:
        grid[r][c] = 0

    return len(flashed)


def main():
    grid = []
    with open('input.txt') as f:
        for line in f:
            grid.append(list(map(int, list(line.rstrip()))))

    flashes = 0
    steps = 0
    while flashes < 100:
        flashes = step(grid)
        steps += 1

    print(steps)


if __name__ == "__main__":
    main()
