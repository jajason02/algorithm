"""
완전탐색의 경우: 2중 for문으로 첫 일꾼이 캐는 벌통 정한다.
이후, 2중 for문을 하나 더 사용해 두번째 일꾼이 캐는 벌통을 정한다.
두 벌통에서 캘 수 있는 최대 벌꿀의 양을 정하고, 수익을 구한다.
반복하여 벌꿀의 수익의 합이 최대가 되는 경우를 구한다.

시간복잡도: 
- 두 일꾼이 벌통을 정하는 경우 : O(N^2) * O(N^2) = O(N^4)
- 각 경우에서 고르는 벌통의 경우의 수 (탐욕적 선택): O(M)
--> 총 O(N^4 * M)
"""

import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # N: 행렬의 크기, M: 선택할 수 있는 벌통의 개수, C: 최대 양
    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_honey = 0  # 최종 최댓값을 저장할 변수

    def get_max_profit(hives):
        """
        부분집합 완전탐색으로 최대 수익을 계산하는 함수
        - 모든 부분집합을 탐색하여 합이 C 이하인 경우 중 수익(제곱합)이 최대인 경우 반환
        - hives: 선택 가능한 벌통 리스트
        """
        best = 0
        # 비트마스킹으로 모든 부분집합 탐색 (2^M 가지)
        for bit in range(1 << len(hives)):
            total = 0   # 선택한 벌꿀의 합
            profit = 0  # 선택한 벌꿀의 수익(제곱합)
            for k in range(len(hives)):
                # k번째 비트가 1이면 해당 벌통 선택
                if bit & (1 << k):
                    total += hives[k]
                    profit += hives[k] ** 2
            # 합이 C 이하인 경우만 유효한 선택
            if total <= C:
                best = max(best, profit)
        return best

    # 첫번째 일꾼이 캘 벌통 정하기
    for i1 in range(N):
        for j1 in range(N - M + 1):
            # 첫번째 일꾼이 채취하는 벌통 (열 범위: j1 ~ j1+M-1)
            first_worker = matrix[i1][j1 : j1 + M]
            first_profit = get_max_profit(first_worker)

            # 두번째 일꾼이 캘 벌통 정하기
            for i2 in range(N):
                for j2 in range(N - M + 1):
                    # 두 벌이 겹치지 않는 조건 확인
                    # 1) 다른 행이면 무조건 OK
                    # 2) 같은 행이면 열 범위가 겹치지 않아야 함
                    if i1 == i2 and not (j1 + M <= j2 or j2 + M <= j1):
                        # 같은 행이면서 열 범위가 겹치는 경우 -> 스킵
                        continue

                    # 두번째 일꾼이 채취하는 벌통 (열 범위: j2 ~ j2+M-1)
                    second_worker = matrix[i2][j2 : j2 + M]
                    second_profit = get_max_profit(second_worker)

                    # 전체 수익 계산 및 최댓값 업데이트
                    total_profit = first_profit + second_profit
                    max_honey = max(max_honey, total_profit)
    
    print(f"#{tc} {max_honey}")