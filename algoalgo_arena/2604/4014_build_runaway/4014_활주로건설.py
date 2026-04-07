import sys

sys.stdin = open("sample.txt", "r")

T = int(input())

def check(lst):
    worked = [0] * N
    for i in range(N-1):
        # 평지면 다음 칸 확인
        if lst[i] == lst[i+1]:
            continue
        # 두 칸 이상 차이나면 False
        if abs(lst[i] - lst[i+1]) > 1:
            return False

        # 내리막
        # 차이 1이면 앞으로 X 칸 확인
        if lst[i] - lst[i+1] == 1:
            # 앞으로 X 칸이 다 같은지 확인
            for k in range(1, X+1): # 1부터 X까지 확인
                if i + k >= N or lst[i] != lst[i + k] + 1 or worked[i + k]:
                    return False
                worked[i + k] = 1
            
        # 오르막       
        # 차이 1이면 앞으로 X 칸 확인
        elif lst[i] - lst[i+1] == -1:
            # 앞으로 X 칸이 다 같은지 확인
            for k in range(0, X):
                if i - k < 0 or lst[i] != lst[i - k] or worked[i - k]:
                    return False
                worked[i - k] = 1        
    return True



for tc in range(1, T+1):
    N, X = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N):
        if check(matrix[i]):
            answer += 1
    for j in range(N):
        temp = [matrix[n][j] for n in range(N)]
        if check(temp):
            answer += 1

    print(f"#{tc} {answer}")
                
                
    
