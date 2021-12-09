#!/usr/local/bin/python3

def find_low_points(arr: [[int]]):
    low = []
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if r > 0 and arr[r][c] >= arr[r-1][c]:
                continue
            if r < len(arr) - 1 and arr[r][c] >= arr[r+1][c]:
                continue
            if c > 0 and arr[r][c] >= arr[r][c-1]:
                continue
            if c < len(arr[r]) - 1 and arr[r][c] >= arr[r][c+1]:
                continue
            low.append((r,c))
    return low


def visit_neighbors(r, c, visited, arr, ids):
    if 0 <= r < len(arr) and 0 <= c < len(arr[r]) and not visited[r][c] and arr[r][c] != 9:
        visited[r][c] = ids
        visit_neighbors(r-1,c,visited,arr, ids)
        visit_neighbors(r+1,c,visited,arr, ids)
        visit_neighbors(r,c-1,visited,arr, ids)
        visit_neighbors(r,c+1,visited,arr, ids)


def main():
    arr = []
    with open('input.txt') as f:
        for line in f:
            arr.append(list(map(int, list(line.rstrip()))))

    visited = [[0 for col in range(len(arr[0]))] for row in range(len(arr))]
    ids = 1
    for p in find_low_points(arr):
        r,c = p
        visit_neighbors(r,c,visited,arr,ids)
        ids += 1

    totals = {}
    for r in range(len(visited)):
        for c in range(len(visited[r])):
            if visited[r][c]:
                ids = visited[r][c]
                totals[ids] = totals.get(ids, 0) + 1
    tot = 1
    for v in sorted(totals.values())[-3:]:
        tot = tot*v
    print(tot)

if __name__ == "__main__":
    main()

