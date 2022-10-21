import sys
sys.stdin = open('input.txt')

'''
   N*N 크기의 판
   돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정
   [입력]
        각 테스트 케이스의 첫번째 줄에는 하나의 정수 N(5 <= N <= 20)
        다음 N개의 줄의 각 줄에는 길이 N인 문자열이 주어짐
'''

T = int(input())
for idx in range(T):
    N = int(input())
    N_list = [list(input()) for _ in range(N)]
    result = 'NO'
    rb_count = 0
    rt_count = 0
    for i in range(N):
        if result == 'YES':
            break

        if N_list[i][i] == 'o':
            rb_count += 1
        else :
            rb_count = 0

        if N_list[i][N-1-i] == 'o':
            rt_count += 1
        else :
            rt_count = 0

        if rt_count >= 5 :
            result = 'YES'
            break
        if rb_count >= 5 :
            result = 'YES'
            break
        row_count = 0
        col_count = 0
        for j in range(N):
            if N_list[i][j] == 'o':
                row_count += 1
            else :
                row_count = 0
            if N_list[j][i] == 'o':
                col_count += 1
            else :
                col_count = 0
            if row_count >= 5:
                result = 'YES'
                break
            if col_count >= 5:
                result = 'YES'
                break

    print('#{} {}'.format(idx+1, result))

    ############################################################



