import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]
    success_col = data[99].index(2)
    ni, nj = 99, success_col
    result = 0

    while ni > 0 :
        visited[ni][nj] = 1
        if nj-1 >= 0 and data[ni][nj-1] and visited[ni][nj-1] == 0 :
            nj -= 1
            continue
        elif nj+1 <=99 and data[ni][nj+1] and visited[ni][nj+1] == 0 :
            nj += 1
            continue
        else :
            ni -= 1
    result = nj
    print('#{} {}'.format(tc, result))