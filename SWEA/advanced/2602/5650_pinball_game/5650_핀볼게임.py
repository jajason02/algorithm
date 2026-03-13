import sys

sys.stdin = open("sample_input.txt", "r")


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

direction = [
    [],
    [1, 3, 0, 2],
    [3, 0, 1, 2],
    [2, 0, 3, 1],
    [1, 2, 3, 0],
    [1, 0, 3, 2]
]



T = int(input())

for tc in range(1, T+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
