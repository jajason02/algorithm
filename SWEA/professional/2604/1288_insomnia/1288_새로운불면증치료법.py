"""
완전탐색의 풀이: 수를 N배 한 후, 각 자리 수를 모두 세어 없으면 리스트에 추가, 리스트를 확인 후
0~9가 다 있으면 풀이 완료. 연산 횟수 O(klog k)
"""

import sys
sys.stdin = open("sample.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 카운팅배열. 인덱스가 0~9를 의미, 수가 나오면 1로 변경
    num_lst = [0]*10
    iter = 0
    # 루프 반복 O(k)
    # any num_lst 검사 = O(10) = O(1)
    while any(x == 0 for x in num_lst):
        iter += 1
        # 숫자 -> 문자열 O(자리수) -> O(log k)
        temp = str(N * iter)
        # 각 자리 검사 O(자리수)
        for n in temp:
            if num_lst[int(n)] == 0:
                num_lst[int(n)] = 1
        
    print(f"#{tc} {N * iter}")