import sys

sys.stdin = open("sample_input(2).txt", "r")

T = int(input())


def babygin(lst1, lst2):
    n, m = len(lst1), len(lst2)
    babygin_1 = 0
    babygin_2 = 0
    count_1 = [0] * 10
    count_2 = [0] * 10
    
    for i in range(0, n - 2):
        if lst1[i] == lst1[i + 1] == lst1[i + 2]:
            babygin_1 = 1
            return (babygin_1, babygin_2)
    for i in range(0, n - 2):
        if lst2[i] == lst2[i + 1] == lst2[i + 2]:
            babygin_2 = 1
            return (babygin_1, babygin_2)

    for n in range(len(lst1)):
        count_1[lst1[n]] += 1
    for n in range(len(lst2)):
        count_2[lst2[n]] += 1
        
    for i in range(0, 8):
        if count_1[i] and count_1[i + 1] and count_1[i + 2]:
            babygin_1 = 1
            return (babygin_1, babygin_2)

    for i in range(0, 8):
        if count_2[i] and count_2[i + 1] and count_2[i + 2]:
            babygin_2 = 1
            return (babygin_1, babygin_2)


    return (babygin_1, babygin_2)


for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    player1, player2 = [], []
    winner = 0

    for i in range(len(lst)):
        if i % 2:
            player2.append(lst[i])
        else:
            player1.append(lst[i])

        if i >= 6:
            player1.sort()
            player2.sort()

            result = babygin(player1, player2)

            if result == (1, 0):
                winner = 1
                break
            elif result == (0, 1):
                winner = 2
                break
            elif result == (1, 1):
                break

    print(f"#{tc} {winner}")
