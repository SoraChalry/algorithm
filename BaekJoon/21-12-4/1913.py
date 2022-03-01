import sys
input = sys.stdin.readline

n = int(input())
target = int(input())
lst = list(list(0 for _ in range(n)) for _ in range(n))

delta = [(1,0),(0,1),(-1,0),(0,-1)]

m = 0
i, j = 0, 0
x, y = 0, 0
sn = n*n
lst[i][j] = sn

while sn > 1:
    ni = i + delta[m][0]
    nj = j + delta[m][1]

    if 0<=ni<n and  0<=nj<n and not lst[ni][nj]:
        sn -= 1
        lst[ni][nj] = sn
        if sn == target:
            x, y = ni, nj
        i, j = ni, nj
    else :
        m = (m+1) %4

for k in lst:
    print(*k)
print(x+1, y+1)