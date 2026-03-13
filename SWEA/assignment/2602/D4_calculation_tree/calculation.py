def calculate_tree(node_idx):

    node = tree[node_idx]
    
    # 노드 정보가 숫자 하나만 들어있는 경우 (Leaf Node)
    if len(node) == 1:
        return float(node[0])
    
    # 노드 정보가 [연산자, 왼쪽자식, 오른쪽자식] 인 경우
    operator = node[0]
    left_val = calculate_tree(int(node[1]))   # 왼쪽 자식 결과 가져오기
    right_val = calculate_tree(int(node[2]))  # 오른쪽 자식 결과 가져오기
    
    # 연산자에 따른 계산 수행
    if operator == '+':
        return left_val + right_val
    elif operator == '-':
        return left_val - right_val
    elif operator == '*':
        return left_val * right_val
    elif operator == '/':
        return left_val / right_val


for tc in range(1, 11):
    N = int(input())
    tree = {}
    
    # 트리 구조 생성
    for _ in range(N):
        info = input().split()
        node_num = int(info[0])
        # 노드 번호를 제외한 나머지 정보(값, 자식번호들)를 저장
        tree[node_num] = info[1:]
    
    # 루트 노드(1번)부터 계산 시작
    # 최종 결과는 정수형으로 출력 (소수점 아래 버림)
    result = int(calculate_tree(1))
    print(f"#{tc} {result}")