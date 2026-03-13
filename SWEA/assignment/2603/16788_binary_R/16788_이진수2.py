T = int(input())

for tc in range(1, T+1):
    N = float(input())

    bin = ""
    cnt = 0
    while N:
        N = N * 2
        if N >= 1:
            N -= 1
            bin = bin + "1"
        else:
            bin = bin + "0"
        cnt += 1
        if cnt > 12:
            bin = "overflow"    
            break
    print(f"#{tc} {bin}")
