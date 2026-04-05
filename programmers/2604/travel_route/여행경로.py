def solution(tickets):
    answer = []
    tickets.sort()  # 알파벳 순 정렬 → 탐색 순서 보장
    visited = [False] * len(tickets)
    
    def dfs(cur, path):
        # 모든 티켓 사용 완료
        if len(path) == len(tickets) + 1:
            answer.append(path[:])
            return
        
        for i, (src, dst) in enumerate(tickets):
            # 이미 쓴 티켓이거나 출발지 불일치면 스킵
            if visited[i] or src != cur:
                continue
            visited[i] = True
            path.append(dst)
            dfs(dst, path)
            # 백트래킹
            path.pop()
            visited[i] = False
    
    dfs("ICN", ["ICN"])
    
    # 가능한 경로 중 알파벳 순 가장 빠른 것 반환
    return sorted(answer)[0]