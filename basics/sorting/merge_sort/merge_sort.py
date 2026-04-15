arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)


# 정렬 함수 시작
def merge_sort(start, end):
    # start: 집합의 맨 왼쪽 인덱스
    # end: 집합의 맨 오른쪽 인덱스
    # 부분집합이 1개가 될 때 까지 나눈다(start와 end의 차이가 1)
    if start == end - 1:
        return start, end

    # 중앙값`mid`을 기준으로 반으로 계속 나눈다
    mid = (start + end) // 2
    # mid의 왼쪽 부분집합 나누기
    left_s, left_e = merge_sort(start, mid)
    # mid의 오른쪽 부분집합 나누기
    right_s, right_e = merge_sort(mid, end)
    # 병합, 정렬 함수 실행
    merge(left_s, left_e, right_s, right_e)
    # 병합 후 양 끝 인덱스 리턴
    return start, end


# 부분집합을 병합, 정렬하는 함수
# left_s, left_e: 좌측 부분집합의 시작, 끝 인덱스
# right_s, right_e: 우측 부분집합의 시작, 끝 인덱스
def merge(left_s, left_e, right_s, right_e):
    # l: left 부분집합의 시작 인덱스
    # r: right 부분집합의 시작 인덱스
    l = left_s
    r = right_s
    # N: 집합 원소 개수
    N = right_e - left_s
    # result: 병합된 집합 임의로 저장하는 리스트
    result = [0] * N
    # idx: result에 정렬된 원소 개수
    idx = 0
    """
    좌, 우 부분집합의 시작 인덱스부터 비교 시작
    크기가 작은 원소부터 result 리스트에 추가
    추가 후 idx, l, r 인덱스를 1씩 증가
    l, r 인덱스가 각각 left_e, right_e가 될 때까지 반복
    마지막으로 정렬, 병합된 result 리스트를 arr 리스트에 재할당
    """
    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            l += 1
            idx += 1
        else:
            result[idx] = arr[r]
            r += 1
            idx += 1

    while r < right_e:
        result[idx] = arr[l]
        r += 1
        idx += 1

    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1

    for i in range(N):
        arr[left_s + i] = result[i]

    print(result)

merge_sort(0, N)

print(arr)