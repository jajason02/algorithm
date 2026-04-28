"""
완전풀이: N을 이진수로 바꾸고 맨 끝에서 한 줄씩 문자가 1인지 아닌지 비교
비트마스킹으로 맨 끝에서부터 M & (1 << N) == 1인지 비교할거임 

피드백: for문으로 1인지 하나하나 비교하지 말고 한꺼번에 하자
"""

import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     for n in range(N):
#         if M & (1 << n) == 0:
#             ans = "OFF"
#             break
#     else:
#         ans = "ON"
#     print(f"#{tc} {ans}")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # lastNBit: 마지막 N개의 비트가 모두 1인 수
    lastNBit = (1 << N) - 1         # 111...1 (길이 N)
    if lastNBit == (M & lastNBit):
        print(f'#{test_case} ON')
    else:
        print(f'#{test_case} OFF')