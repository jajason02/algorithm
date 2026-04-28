import sys
sys.stdin = open("sample_input.txt", "r")

# def edit(lst: list, cmd, x):
#     global idx
#     # command[i]를 꺼내 명령어를 실행
#     # 명령어가 I일 경우 원소 추가
#     if cmd == "I":
#         y = int(command[idx][2])
#         lst.insert(x, y)
#     # 명령어가 D일 경우 원소 제거
#     elif cmd == "D":
#         lst.pop(x)
#     # 명령어가 C일 경우 원소 교체
#     elif cmd == "C":
#         y = int(command[idx][2])
#         lst[x] = y


# T = int(input())
# for tc in range(1, T+1):
#     # N: 수열의 길이  M: 추가 횟수  L: 출력할 인덱스 번호
#     N, M, L = map(int, input().split())
#     seq = list(map(int, input().split()))  #seq: 수열 리스트
#     command = []  # command: 편집 명령어 리스트
#     for i in range(M):
#         temp = input().split()
#         command.append(temp)

#     idx = 0
#     for _ in range(M):
#         cmd = command[idx][0]
#         x = int(command[idx][1])
#         edit(seq, cmd, x)
#         idx += 1
#     if len(seq) < L:
#         print(f"#{tc} -1")
#     else:
#         print(f"#{tc} {seq[L]}")
    
class NODE:
    def __init__(self, v=0, prev=None, next=None):
        self.v = v
        self.prev = prev
        self.next = next

def input_f():
    global cnt, head
    global n, Q, L

    n, Q, L = map(int, input().split())
    cur = head
    input_lst = list(map(int, input().split()))
    for i in range(n):
        if i == 0:
            head = NODE(input_lst[i], None, None)
            cur = head
        else:
            cur.next = NODE(input_lst[i], cur, None)
            cur = cur.next

        cnt += 1

def pro():
    global cnt, head

    for _ in range(Q):
        input_line = input().split()
        ch = input_line[0]
        if ch == 'C':
            cur = head
            y, s = int(input_line[1]), int(input_line[2])
            for i in range(y):
                cur = cur.next
            cur.v = s
        elif ch == 'I':
            x, y = int(input_line[1]), int(input_line[2])
            x -= 1
            if x == -1:
                if cnt > 0:
                    newNode = NODE(y, 0, head)
                    head.prev = newNode
                    head = newNode
                else:
                    head = NODE(y, 0, 0)
            else:
                cur = head
                for i in range(x):
                    cur = cur.next
                node = NODE(y, cur, cur.next)
                if cur.next:
                    cur.next.prev = node
                cur.next = node

            cnt += 1
        elif ch == 'D':
            x = int(input_line[1])
            cur = head
            for i in range(x):
                cur = cur.next
            prev = cur.prev
            next = cur.next
            if prev:
                prev.next = next
            if next:
                next.prev = prev
            if prev == None:
                head = next
            cnt -= 1

    cur = head
    for i in range(L):
        if cur == None:
            break

        cur = cur.next

    if cur == None:
        print(-1)
    else:
        print(cur.v)

TT = int(input())
for tt in range(1, TT + 1):
    head = NODE()
    cnt = 0
    input_f()
    print(f'#{tt} ', end='')
    pro()