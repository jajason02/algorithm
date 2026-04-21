"""
1시간 후 이동방향에 있는 다음 셀로 이동. 약품에 닿으면 절반이 죽고 이동방향이 반대로 바뀜
두개의 군집이 한 셀에 모이는 경우 군집이 합쳐짐. 이동 방향은 미생물 수가 가장 많은 군집의 이동방향

"""

# import sys
# sys.stdin = open("sample_input.txt", "r")

# 방향리스트 상 하 좌 우
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

# 반대방향
dir_switch = {1: 2, 2: 1, 3: 4, 4: 3}


# 약품에 닿는 경우
def check_edge(i, j):
    if i == 0 or i == N - 1 or j == 0 or j == N - 1:
        return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    # N: 셀의 개수  M: 격리 시간  K: 미생물 군집의 개수
    N, M, K = map(int, input().split())
    # 세로, 가로, 미생물 수, 이동 방향
    micro_info = [list(map(int, input().split())) for _ in range(K)]

    for t in range(M):
        n_dict = {}
        for n in range(len(micro_info)):
            # 리스트 순회하면서 다음 칸 체크
            ci, cj, num, d = micro_info[n]
            ni, nj = ci + di[d], cj + dj[d]
            # 엣지에 닿았으면 미생물 수 반토막, 방향 반대로
            if check_edge(ni, nj):
                # 좌표가 딕셔너리에 없으면 생성
                if (ni, nj) not in n_dict.keys():
                    n_dict[(ni,nj)] = [num//2, dir_switch[d]]
                # 있으면 추가
                else:
                    n_dict[(ni,nj)] += [num//2, dir_switch[d]]
            # 안닿으면 전진
            else:
                if (ni, nj) not in n_dict.keys():
                    n_dict[(ni,nj)] = [num, d]
                else:
                    n_dict[(ni,nj)] += [num, d]
        micro_info = []
        for key, item in n_dict.items():
            if len(item) == 2:
                micro_info.append([key[0], key[1], item[0], item[1]])
            else:
                micro_num = sum(item[::2])
                n_d = item[item.index(max(item[::2]))+1]
                micro_info.append([key[0], key[1], micro_num, n_d])
    # print(micro_info)       
    lst = [micro_info[i][2] for i in range(len(micro_info))]  
    # print(lst)
    print(f'#{tc} {sum(lst)}')
                
