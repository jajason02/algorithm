# import sys

# sys.stdin = open("input.txt", "r")

T = int(input())

# 백트래킹 함수
def backtracking(idx, prob):
    
    pass

for tc in range(1, T + 1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 최댓값을 저장하는 변수 max_prob
    # 이미 작업을 한 직원의 인덱스를 selected에 저장
    
    mem = [-1] * (1 << N)

    # 최초값이 왜 100이여 샹
    backtracking(0, 100)
    print(f"#{tc} {max_prob:.6f}")


"""
T = int(input())
 
def solve(i, task):
    if task == (1 << N) - 1:
        return 1  # 100%를 1로 표현
 
    if mem[task] != -1:
        return mem[task]
 
    max_prob = 0  # 최대 확률 저장
 
    for j in range(N):
        if work[i][j] and not task & (1 << j):  # 아직 할당되지 않은 작업일 때
            max_prob = max(max_prob, work[i][j] * solve(i + 1, task | (1 << j)))
 
    mem[task] = max_prob  # 메모이제이션
    return max_prob
 
 
for tc in range(1, T + 1):
    N = int(input())
 
    work = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
     
    # 비트마스크 기반 메모이제이션, -1로 초기화
    mem = [-1] * (1 << N)
 
    print(f"#{tc} {solve(0, 0) * 100:.6f}")
    
"""
