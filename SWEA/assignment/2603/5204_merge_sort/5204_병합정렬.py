# import sys

# sys.stdin = open("sample.txt", "r")

T = int(input())


# 병합정렬 구현. 먼저 리스트를 부분집합으로 나누는 과정 구현
# start, end = 부분집합 원소들의 첫번째, 마지막 원소의 인덱스
def mergesort(start, end):

    # 부분집합의 크기가 1일때(start-end = 1) 함수 리턴
    if start == end - 1:
        return start, end
    # 부분집합을 반으로 나누는 인덱스 mid 생성
    mid = (start + end) // 2

    # 부분집합을 반으로 나누어 재귀 실행
    left_s, left_e = mergesort(start, mid)
    right_s, right_e = mergesort(mid, end)

    # 부분집합 둘을 다시 합치면서 정렬하는 함수 실행
    merge(left_s, left_e, right_s, right_e)

    # 병합정렬 함수 실행 후 start, end 인덱스 출력
    return start, end


# 병합정렬에서 부분집합을 합치면서 정렬하는 함수
# left_s, left_e = 왼쪽 부분집합의 처음, 마지막 원소 인덱스
# right_s, right_e = 오른쪽 부분집합의 처음, 마지막 원소 인덱스
def merge(left_s, left_e, right_s, right_e):
    global count
    # l, r 부분집합간의 값을 비교하는 인덱스. 부분집합의 첫번째 원소 인덱스로 지정
    l = left_s
    r = right_s
    # 합친 후 리스트의 길이
    n = right_e - left_s
    # 정렬된 후의 원소를 저장하는 리스트 result와 정렬된 원소의 수를 나타내는 인덱스
    idx = 0
    result = [0] * n

    # 병합정렬 시 왼쪽 부분집합의 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의수 카운트
    if lst[left_e - 1] > lst[right_e - 1]:
        count += 1

    # 오른쪽 왼쪽 모두 원소가 남아있는 경우
    # 한 쪽의 원소가 모두 사라질 때 까지 값을 비교한 후 result에 append
    while l < left_e and r < right_e:
        if lst[l] > lst[r]:
            result[idx] = lst[r]
            r += 1
            idx += 1
        else:
            result[idx] = lst[l]
            l += 1
            idx += 1

    # 왼쪽 부분집합의 원소만 남은 경우
    while l < left_e:
        result[idx] = lst[l]
        l += 1
        idx += 1

    # 오른쪽 부분집합의 원소만 남은 경우
    while r < right_e:
        result[idx] = lst[r]
        r += 1
        idx += 1

    # 병합정렬이 일어난 후의 리스트 result를 원래 있던 lst에 재할당
    for i in range(n):
        lst[left_s + i] = result[i]


for tc in range(1, T + 1):
    # 리스트의 원소의 수 입력
    N = int(input())
    # 정렬이 필요한 리스트 입력
    lst = list(map(int, input().split()))

    # 문제에서 요구되는 값 count
    count = 0
    mergesort(0, N)

    print(f"#{tc} {lst[N//2]} {count}")
