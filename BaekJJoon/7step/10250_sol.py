T = int(input())
for tc in range(1, T+1):
    H,W,N = map(int, input().split())
    a = N % H
    b = N // H

    if a == 0 :
        a = H
    elif a > 0:
        b += 1
    floor_text = ''
    floor_text = str(a)+str(b).zfill(2 if len(str(W))==1 else len(str(W)))
    print(floor_text)