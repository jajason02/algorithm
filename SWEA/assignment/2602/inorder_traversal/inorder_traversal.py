T = 10

for tc in range(1, T + 1):
    # 노드의 개수
    N = int(input())

    # 왼쪽 자식
    cleft = [0] * (N + 1)
    # 오른쪽 자식
    cright = [0] * (N + 1)

    # 어떤 인덱스에 어떤 알파벳이 있는지 확인
    node = [0] * (N + 1)
    # node[1] => 1번 노드에 저장된 알파벳은 무엇인가?
    # node[1] == 'A' : 1번 노드에 저장된 알파벳은 A

    for i in range(N):
        # 한 줄에 노드 하나의 정보가 들어옴
        # 노드 번호, 알파벳, 왼쪽, 오른쪽
        # 한 줄 입력을 다 받아놓고 쪼개서 개수를 센 다음에 개수에 맞게 처리
        info = input().split()
        # info의 길이가 2 : 단말노드(잎 노드), 자식 노드가 없음
        # info의 길이가 3 : 자식노드가 1개 있음(왼쪽)
        # info의 길이가 4 : 자식노드가 2개 있음(왼, 오)
        p = int(info[0])
        alpha = info[1]
        node[p] = alpha

        # 길이가 3 이상인 경우(자식 노드가 있는 경우)
        if len(info) >= 3:
            # 왼쪽 자식
            cleft[p] = int(info[2])
            # 길이가 4면
            if len(info) == 4:
                # 오른쪽 자식도 있음
                cright[p] = int(info[3])

        # 문제에서 원하는 답 구하기
        answer = ""

    # 중위순회
    def inorder(t):
        global answer
        # t번 노드가 존재한다면
        if t:
            # t번 노드의 왼쪽 서브트리 탐색 : L
            inorder(cleft[t])
            # t번 노드 방문 처리 : V
            # t번 노드에 써져있는 알파벳을 이어붙이기
            answer += node[t]
            # t번 노드의 오른쪽 서브트리 탐색 : R
            inorder(cright[t])

    inorder(1)

    print(f"#{tc} {answer}")