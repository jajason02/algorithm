# 이진 탐색 트리(BST, Binary Search Tree)
- 평균 O(log n)의 속도로 검색 가능, 최악의 경우(한쪽으로 치우친 경사 이진 트리) O(n)의 시간이 걸림
- 탐색 작업을 효율적으로
- 모든 원소는 서로 다른 유일한 키를 가짐
- key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
- 중위 순회 시 오름차순으로 정렬된 값
- 탐색, 삽입 삭제 시간은 트리의 높이만큼 시간이 걸림
```python
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


# root 노드에서 시작, key 값을 가진 노드 찾기
# 어떤 서브트리의 루트 노드
def search(root, key):

    # key 값과 루트 노드 비교
    if key == root.key:
        return root

    # key 값이 더 크다면
    if root.key < key:
        # 내가 찾는 key 값이 루트의 키 값보다 크면 오른쪽으로
        return search(root.right, key)

    # key 값이 더 작다면
    if root.key > key:
        return search(root.left, key)


def insert(root, key):
    # 트리가 없는 상태, 루트 노드에 key 삽입
    if root is None:
        return TreeNode(key)
    # 루트 노드가 있다면, key 값 탐색 후 탐색 실패한 위치에 key값 가진 노드 삽입
    else:
        # 우리가 삽입하려고 하는 key가 루트보다 작은 경우
        if key < root.key:
            root.left = insert(root.left, key)
        # 큰 경우
        else:
            root.right = insert(root.right, key)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end = " ")
        inorder(root.right)

arr = [9, 4, 12, 3, 6, 15, 13, 17]

root = insert(None, arr[0])
for num in arr[1:]:
    insert(root, num)

inorder(root)
```