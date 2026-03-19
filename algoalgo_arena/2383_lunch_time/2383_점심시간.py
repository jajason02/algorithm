import sys

sys.stdin = open("small.txt", "r")

T = int(input())


def stair_select(idx):
    if idx == len(people):
        solve()
        return
    for n in range(2):
        selected[idx] = n
        stair_select(idx + 1)

    
def move_time(tup, idx):
    return abs(tup[0]-stair[idx][0]) + abs(tup[1]-stair[idx][1])


def solve():
    stair_1 = []
    stair_2 = []
    for n in range(len(people)):
        if selected[n] == 0:
            stair_1.append((n, move_time(people[n], 0)))
        elif selected[n] == 1:
            stair_2.append((n, move_time(people[n], 1)))
    print(stair_1)
    print(stair_2)
    t = 1
    L_1 = stair[0][2]
    L_2 = stair[1][2]

    arrived_q1 = []
    stair_q1 = []
    arrived_q2 = []
    stair_q2 = []

    t = 
    
                    

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stair = []
            
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                people.append((i, j))
            elif matrix[i][j] > 1:
                stair.append((i, j, matrix[i][j]))
    selected = [0] * len(people)

    stair_select(0)
    
    
