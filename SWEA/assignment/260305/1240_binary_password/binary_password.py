import sys

sys.stdin = open("input.txt", "r")

T = int(input())

password_code = {
    "0001101" : "0",
    "0011001" : "1",
    "0010011" : "2",
    "0111101" : "3",
    "0100011" : "4",
    "0110001" : "5",
    "0101111" : "6",
    "0111011" : "7",
    "0110111" : "8",
    "0001011" : "9",
}

for tc in range(1, T+1):
    N , M = map(int, input().split())

    matrix = [input() for _ in range(N)]
    found = False
    for i in range (N):
        if found: break
        for j in range(M - 1, 54, -1):
            if matrix[i][j] == "1":
                line = matrix[i][j - 55: j + 1]
                line = password_code[line[0:7]] + password_code[line[7:14]] + password_code[line[14:21]] + password_code[line[21:28]] + password_code[line[28:35]] + password_code[line[35:42]] + password_code[line[42:49]] + password_code[line[49:56]]
                if (sum(map(int, line[::2]))*3 + sum(map(int, line[1::2]))) % 10 == 0:
                    answer = sum(map(int, line))
                else:
                    answer = 0
                found = True
                break
    print(f"#{tc} {answer}")
                