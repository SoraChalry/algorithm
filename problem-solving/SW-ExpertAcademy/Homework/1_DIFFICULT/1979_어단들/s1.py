import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    cnt_row = 0
    cnt_col = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt_row += 1
            if arr[i][j] == 0 or j == N-1:
                if cnt_row == K:
                    result += 1
                cnt_row = 0

            if arr[j][i] == 1:
                cnt_col += 1
            if arr[j][i] == 0 or j == N-1:
                if cnt_col == K:
                    result += 1
                cnt_col = 0
    print('#{} {}'.format(tc, result))
