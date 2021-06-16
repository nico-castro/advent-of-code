#!/usr/local/bin/python3

def convert_row(row: str) -> int:
    bins = ''
    for char in row:
        if char == 'F':
            bins = bins + '0'
        elif char == 'B':
            bins = bins + '1'
        else:
            raise ValueError(f"Got row: {row}")
    return int(bins, 2)

def convert_col(col: str) -> int:
    bins = ''
    for char in col:
        if char == 'L':
            bins = bins + '0'
        elif char == 'R':
            bins = bins + '1'
        else:
            raise ValueError(f"Got col: {col}")
    return int(bins, 2)

def seat_id(row: int, col: int) -> int:
    return row*8+col


def main():
    highest = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            row = convert_row(line[0:7])
            col = convert_col(line[-3:])
            seat = seat_id(row, col)
            # print(f"{line}: row {row}, column {col}, seat ID {seat_id(row, col)}")
            if seat > highest:
                highest = seat
    print(highest)


if __name__ == "__main__":
    main()
