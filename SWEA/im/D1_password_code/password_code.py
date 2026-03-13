T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input()))
    M = int(input())
    pass_list = list(map(int, input()))
    """
    리스트 안에 찾는 숫자가 있으면
    리스트 슬라이싱을 통해 그 숫자와 앞부분을 제거한다
    """
    for m in pass_list:
        if m not in num_list:               
            answer = 0
            break
        else:
            num_list = num_list[num_list.index(m)+1:]
    else:
        answer = 1

    print(f"#{tc} {answer}")