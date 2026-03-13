# import sys

# sys.stdin = open("sample_input(2).txt", "r")

T = int(input())


# 베이비진 체크
def baby_gin(lst):
    # 카운팅 배열 사용
    counts = [0] * 10
    for n in range(len(lst)):
        counts[lst[n]] += 1

    # 같은 수가 3개 이상 나오면 베이비진
    for i in range(10):
        if counts[i] >= 3:
            return True
            
    # 연속된 수가 3개 나오면 베이비진
    for i in range(8):
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            return True
    # 베이비진 아님
    return False


for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    player1, player2 = [], []
    # 승자(무승부 시 0 출력)
    winner = 0

    # 카드 나눠 갖기(홀수번째: player1)
    for i in range(len(lst)):
        if i % 2:
            player2.append(lst[i])
        else:
            player1.append(lst[i])
        # 6장 받았을 때 부터 베이비진 확인(5장때 바로 해도 되는지 몰겠네)
        if i >= 6:
            player1.sort()
            player2.sort()
            # 누가 이겼는지 확인(없으면 기본값(무승부 0) 출력)
            if baby_gin(player1) and not baby_gin(player2):
                winner = 1
            elif not baby_gin(player1) and baby_gin(player2):
                winner = 2
    
    print(f"#{tc} {winner}")
