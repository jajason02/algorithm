"""
AI도움: 튜플로 형변환 해서 check 집합에 값을 넣고 가지치기 하는 방법을 도움받았다.
리스트를 다시 문자열로 돌리는 방법 기억이 안나서 도움 받음.
"""

T = int(input())


# 교환횟수k 를 단계로
def solve(k):
    global max_price
    # 가지치기
    if (k, tuple(num_lst)) in check:
        return

    # 종료
    if k == cnt:
        # 만든 숫자가 최대값인가? 비교해서 갱신
        max_price = max(max_price, int("".join(num_lst)))
        return

    # 재귀호출(다음단계)
    # 자리를 교환해서 다음 단계(다음 교환횟수)
    # 앞쪽자리 인덱스 i : 0 ~ N-2
    # 뒤쪽자리 인덱스 j : i+1 ~ N-1
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
            solve(k + 1)
            # check에 다음 숫자판과 단계를 입력하여 가지치기에 활용
            check.add((k + 1, tuple(num_lst)))
            # 다시 돌려놓기
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]


for tc in range(1, T + 1):
    # numbers : 처음 숫자
    numbers, cnt = input().split()
    # 교환횟수
    cnt = int(cnt)
    # 문자열을 리스트로 전환
    num_lst = list(numbers)
    N = len(numbers)

    max_price = 0

    # 세트안에는 (교환횟수k, k번교환해서만든숫자열) 튜플로 저장
    # 3번의 교환을 통해서 "12345" 라는 숫자열을 이전에 만든적이 있다면
    # 나중에 교환순서는 다르지만 3번교환을 통해 "12345" 를 만들면
    # 여기서 다시 만드는 모든 숫자열은 중복이 된다.
    check = set()

    # 교환안했으니 교환횟수 0부터 시작
    solve(0)

    print(f"#{tc} {max_price}")
