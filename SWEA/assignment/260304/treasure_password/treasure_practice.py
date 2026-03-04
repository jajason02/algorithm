# import sys

# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # 비밀번호 문자열
    treasure = input()
    # 비밀번호를 저장하는 리스트 생성
    password_lst = []
    # 비밀번호의 길이//4 만큼 반복, 예를들어 28글자면 7번 로테이션을 돌린다)
    for _ in range(N//4):
        # 4번 문자열을 잘라서 비밀번호 10진수로 바꿔서 리스트에 추가
        for m in range(4):
            temp = treasure[m * (N // 4) : m * (N // 4) + (N // 4)]
            # 겹치는 숫자는 추가하지 않는다
            if int(temp, 16) not in password_lst:
                password_lst.append(int(temp, 16))
        # 로테이션 돌리기        
        treasure = treasure[1 : N] + treasure[0] 
    # 내림차순으로 비밀번호 정렬
    password_lst.sort(reverse=True)
    print(f"#{tc} {password_lst[K-1]}")
