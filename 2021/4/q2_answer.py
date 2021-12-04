#!/usr/local/bin/python3

def check_row(board, r): 
    for c in range(5):
        if not board[r][c].endswith('x'):
            return False
    return True
def check_col(board, c):
    for r in range(5):
        if not board[r][c].endswith('x'):
            return False
    return True

def winner(board):
     # check rows
    for r in range(5):
        if check_row(board, r):
            return True
    # check cols
    for c in range(5):
        if check_col(board, c):
            return True
    return False

def calc_score(board: [[int]], num: int):
    # parse the winning line
    score = 0
    for r in board:
        for c in r:
            if not c.endswith('x'):
                score += int(c)
    return score*num

def main():
    boards = []
    board = []
    with open('input.txt') as f:
        nums = f.readline().rstrip().split(',')
        for line in f:
            if line == '\n':
                continue
            board.append([b for b in line.rstrip().split(' ') if b != ''])
            if len(board) == 5:
                boards.append(board)
                board = []

    winners = []
    winning_scores = []
    for n in nums:
        for x in range(len(boards)):
            if x in winners:
                continue
            b = boards[x]
            for r in range(5):
                for c in range(5):
                    if b[r][c] == n:
                        b[r][c] = b[r][c]+'x'
            if winner(b):
                winning_scores.append(calc_score(b, int(n)))
                winners.append(x)

    print(winning_scores[-1])

if __name__ == "__main__":
    main()

