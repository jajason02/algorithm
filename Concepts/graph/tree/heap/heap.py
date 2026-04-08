# 최대힙으로 사용할 배열
heap = [0] * 11
# 다음에 넣을 자리 기억을 위해 마지막 번호
# 마지막에 원소를 넣은 자리
last = 0

# 삽입
def enq(i):
    global last

    # i 를 맨 마지막에 추가
    # 맨 마지막 원소 + 1이 마지막 자리
    last += 1
    heap[last] = i

    # 일단 맨 마지막에 넣어봤는데 여기가 니 자리가 맞니??
    # 최대힙: 부모노드 > 자식노드
    # 이 조건을 만족한다면 맞는 자리, 만족하지 않는다면 잘못됨
    # 잘못된 자리면 부모와 자리교환을 통해 맞는 자리를 찾도록
    child = last
    # 완전이진트리 부모노드 번호 = 자식노드 // 2
    parent = child // 2

    # child 노드의 값과 parent 노드의 값을 비교
    # 부모노드가 존재하고, 부모노드가 자식노드보다 작으면 자리 교환
    while parent != 0 and heap[child] > heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]

        # 다음 비교를 위해 부모 자식 업데이트
        child = parent
        parent = child // 2

def deq():
    global last
    # 삭제한 원소를 반환 해야하기 때문에 기억해두기
    root = heap[1]

    # 루트노드 자리에 일단 마지막 노드 놓아보기
    heap[1] = heap[last]
    # 마지막 원소 번호 -1
    last -= 1

    # 일단 마지막 노드를 루트 자리에 놓아봤는데 여기가 니 자리가 맞니
    # 최대힙 : 부모 > 자식
    parent = 1
    child = parent * 2 # 왼쪽 자식

    # 부모 > 자식
    # 이 조건을 만족하도록 계속 바꾸기
    while child <= last:

        # 자식이 두명이면 그중에 큰 자식이랑 비교 하면 된다.
        if child + 1 <= last and heap[child] < heap[child + 1]:
            # 오른쪽 자식이 더 크면 부모노드 비교대상은 오른쪽 자식임
            child = child + 1

        # 자식과 부모 비교해서 부모 > 자식 이 조건을 만족하도록 자리 교환
        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child # 다음 부모 노드
            child = child * 2 # 다음 자식 노드
        else:
            # 부모가 자식보다 크다면 최대힙 조건에 맞음. 자리교환 중단
            break

    # 처음에 기억해 놨던 루트 노드 return
    return root

lst = [6, 5, 4, 1, 3, 2, 9, 8, 7, 10]

for i in range(10):
    enq(lst[i])

print(heap)

for i in range(10):
    print(deq(), end = " ")