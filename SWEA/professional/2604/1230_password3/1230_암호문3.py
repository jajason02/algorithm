"""
완전풀이: 일단 리스트에 암호문 뭉치를 다 저장 후
명령어에 따라 처리기를 제어하는 함수를 만든다
"""

import sys
sys.stdin = open("input.txt", "r")

# T = 10
# for tc in range(1, T+1):
#     # 암호문 개수 N
#     N = int(input())
#     # 암호문 뭉치
#     password_lst = list(map(int, input().split()))
#     # 명령어 개수 M
#     M = int(input())
#     # 명령어
#     command_lst = input().split()
#     for i in range(len(command_lst)):
#         # 원소가 숫자이면 continue
#         # I(삽입)일 때, 앞에서부터 x번째 암호문 바로 다음에 y개 암호문 추가
#         if command_lst[i] == "I":
#             x = int(command_lst[i+1])
#             y = int(command_lst[i+2])
#             for j in range(y):
#                 password_lst.insert(x+j,int(command_lst[i+3+j]))
#         # D(삭제)일 때, 앞에서부터 x번째 암호문 바로 다음부터 y개 암호문 삭제
#         elif command_lst[i] == "D":
#             x = int(command_lst[i+1])
#             y = int(command_lst[i+2])
#             for j in range(y):
#                 password_lst.pop(x)
#         # A(추가)일 때, 암호문 뭉치 맨 뒤에 y개의 암호문 덧붙임
#         elif command_lst[i] == "A":
#             y = int(command_lst[i+1])
#             for j in range(y):
#                 password_lst.append(int(command_lst[i+2+j]))
#     print(f"#{tc}", *password_lst[:10])

def func(lst, cmd, x):
    global idx

    if cmd == 'I':
        y = int(input_line[idx])
        idx += 1

        insertIdx = x
        for i in range(y):
            k = int(input_line[idx])
            idx += 1
            lst.insert(insertIdx, k)
            insertIdx += 1
    elif cmd == 'D':
        y = int(input_line[idx])
        idx += 1

        for i in range(y):
            lst.pop(x)
    elif cmd == 'A':
        for i in range(x):
            y = input_line[idx]
            idx += 1

            lst.append(y)

for tt in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    Q = int(input())
    input_line = input().split()
    # 글로벌 포인터 이게 다르다.
    idx = 0

    for i in range(Q):
        cmd = input_line[idx]
        idx += 1

        x = int(input_line[idx])
        idx += 1

        func(lst, cmd, x)

    print(f'#{tt} ', end='')
    for i in range(10):
        print(lst[i], end=' ')
    print()