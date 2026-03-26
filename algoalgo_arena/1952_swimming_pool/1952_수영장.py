import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    charge = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    plan.append(0)
    plan.append(0)

    quarter_index = -2
    dp = [0] * 15
    for n in range(11, -1, -1):
        dp[n] = min(charge[0] * plan[n] + dp[n+1], charge[1] + dp[n+1], charge[2] + dp[n+3])
    print(f"#{tc} {min(dp[0], charge[3])}")