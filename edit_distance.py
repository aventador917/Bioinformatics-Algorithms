"""
Paul Tang
802713818
CPSC 485
November 18, 2021

Programming Assignment


Prerequisites:
- python 3 is installed (must be python 3+)

Usage:
- open a terminal in the directory of this file
- execute command: python3 edit_distance.py
- input two words and the program will print the result
"""

from typing import List


def edit_distance(word1: str, word2: str) -> (int, List[List[int]]):
    # build the matrix
    matrix = [[0 for j in range(len(word2) + 1)]
              for i in range(len(word1) + 1)]
    # initialize the matrix:
    # the edit distance between empty string "" and any string equals
    # the length of the string
    for i in range(len(word1) + 1):
        matrix[i][0] = i
    for j in range(len(word2) + 1):
        matrix[0][j] = j

    # matrix[i][j] represent the edit distance between word1[0:i] and word2[0:j]
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            # initialize the min distance between between word1[0:i] and word2[0:j]
            # as 1 plus minimum of matrix[i][j-1](delete word2[j]) and
            # matrix[i-1][j] (delete word1[i]) and matrix[i-1][j-1]
            # (change word1[i] to word2[j])
            min_dis = min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1]) + 1
            if word1[i - 1] == word2[j - 1]:
                min_dis = min(min_dis, matrix[i - 1][j - 1])
            matrix[i][j] = min_dis
    return matrix[len(word1)][len(word2)], matrix


def print_matrix(matrix: List[List[int]]) -> None:
    """
    print the distance matrix
    """
    print('The matrix:')
    row, col = len(matrix), len(matrix[0])
    header_row = (' ' * 5) + ' '.join(['{:^5}'.format(i) for i in range(col)])
    print(header_row)
    split_horizontal_line = (' ' * 5) + '-'.join(['-----' for i in range(col)])
    print(split_horizontal_line)
    for i in range(row):
        row_str = '{:>3}'.format(i) + ' |'
        for j in range(col):
            row_str += '{:>4}'.format(matrix[i][j]) + ' :'
        print(row_str)
        print(split_horizontal_line)


def alignment(word1: str, word2: str, dis_matrix: List[List[int]]) -> (str, str):
    w1, w2 = [], []
    row, col = len(dis_matrix) - 1, len(dis_matrix[0]) - 1
    while row > 0 and col > 0:
        if ((word1[row - 1] == word2[col - 1] and dis_matrix[row][col] == dis_matrix[row - 1][col - 1])
                or dis_matrix[row][col] == dis_matrix[row - 1][col - 1] + 1):
            w1.append(word1[row - 1])
            w2.append(word2[col - 1])
            row, col = row - 1, col - 1
        elif dis_matrix[row][col] == dis_matrix[row - 1][col] + 1:
            w1.append(word1[row - 1])
            w2.append('_')
            row = row - 1
        elif dis_matrix[row][col] == dis_matrix[row][col - 1] + 1:
            w1.append('_')
            w2.append(word2[col - 1])
            col = col - 1
    while row > 0:
        w1.append(word1[row - 1])
        w2.append('_')
        row -= 1
    while col > 0:
        w1.append('_')
        w2.append(word2[col - 1])
        col = col - 1
    w1.reverse()
    w2.reverse()
    return ''.join(w1), ''.join(w2)


if __name__ == '__main__':
    word_1 = input('{:>18}'.format("The first  word: "))
    word_2 = input('{:>18}'.format("The second word: "))
    dis, m = edit_distance(word_1, word_2)
    print()
    print_matrix(m)
    print()
    print(f'The edit distance is: {dis}')
    print()
    print('Alignment is:')
    w1, w2 = alignment(word_1, word_2, m)
    print(w1)
    print(w2)
