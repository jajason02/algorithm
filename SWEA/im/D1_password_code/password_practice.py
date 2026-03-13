import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input()))
    M = int(input())
    pass_list = list(map(int, input()))
    for m in pass_list:
        if m not in num_list:
            answer = 0
            break
        else:
            num_list = num_list[num_list.index(m)+1:]
    else:
        answer = 1

    print(f"#{tc} {answer}")