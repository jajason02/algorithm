import sys
sys.stdin = open("sample_input.txt", "r")

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())

def start_point():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == "X":
                return (i, j)
                
def drive(num):
    d = 0
    ci, cj = start
    for n in range(int(command[num][0])):
        # print(n)
        # print(command[num][1][n])
        if command[num][1][n] == "A":
            ci, cj = ci + di[d%4], cj + dj[d%4]
            if 0 > ci or ci >= N or 0 > cj or cj >= N or matrix[ci][cj] == "T":
                ci, cj = ci - di[d%4], cj - dj[d%4]
        elif command[num][1][n] == "L":
            d -= 1
        elif command[num][1][n] == "R":  
            d += 1
    if matrix[ci][cj] == "Y":
        return 1
    else: return 0
        
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    Q = int(input())
    # command = [list(input()) for _ in range(Q)]
    command = [[] for _ in range(Q)]
    for i in range(Q):
        a, b = input().split()
        command[i].append(a)
        command[i].append(b)

    # print(matrix)
    # print(command)
    
    # 출발지점 찾기
    start = start_point()
    
    # 정답
    answer = [0]*Q
    
    for n in range(Q):
        answer[n] = (drive(n))
    print(f"#{tc}", *answer)
        
    