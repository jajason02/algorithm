"""
모든 좌표값에 * 2 하삼
"""

import sys
# sys.stdin = open("sample_input.txt", "r")

# 방향 정의: 0:상(y 증가), 1:하(y 감소), 2:좌(x 감소), 3:우(x 증가)
# 원자 문제는 상하좌우 순서가 미생물과 다르니 주의!
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    atoms = []
    for _ in range(N):
        # x, y, 방향, 에너지
        x, y, d, e = map(int, input().split())
        # 좌표 2배 스케일링 (0.5초 충돌 대비)
        atoms.append([x * 2, y * 2, d, e])

    total_energy = 0
    
    # 원자가 모두 사라지거나 맵 밖으로 나갈 때까지 반복
    # 좌표를 2배 늘렸으므로 최대 4000번의 이동 가능
    for _ in range(4001):
        if len(atoms) < 2: break
        
        # 이동 및 위치 기록
        grid = {}
        for i in range(len(atoms)):
            x, y, d, e = atoms[i]
            nx, ny = x + dx[d], y + dy[d]
            
            # 이동한 위치 업데이트
            atoms[i][0], atoms[i][1] = nx, ny
            
            # 딕셔너리에 좌표별로 원자 인덱스 저장
            if (nx, ny) not in grid:
                grid[(nx, ny)] = []
            grid[(nx, ny)].append(i)
            
        # 충돌 확인 및 처리
        # next_atoms: 다음 반복에 존재하는 원자
        # deleted: 충돌, 범위 이탈로 삭제되는 원자
        next_atoms = []
        deleted = set()
        
        for pos, elements in grid.items():
            # 충돌
            if len(elements) > 1: 
                for idx in elements:
                    # 에너지 흡수
                    total_energy += atoms[idx][3]
                    deleted.add(idx)
            
            # 맵 밖으로 나가는 원자 처리
            else:
                idx = elements[0]
                nx, ny = atoms[idx][0], atoms[idx][1]
                if nx < -2000 or nx > 2000 or ny < -2000 or ny > 2000:
                    deleted.add(idx)

        # 살아남은 원자만 다음 턴으로
        for i in range(len(atoms)):
            if i not in deleted:
                next_atoms.append(atoms[i])
        
        atoms = next_atoms

    print(f"#{tc} {total_energy}")