import sys
sys.stdin = open('input.txt')
'''
    100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램
    [제약 사항]
        총 10개의 테스트 케이스  
        배열의 크기는 100X100으로 동일
        각 행의 합은 integer 범위를 넘어가지 않는다.
        동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
'''
for _ in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_arr = sum(arr[0])
    sum_row = 0
    sum_rtop = 0
    sum_rbottom = 0
    for i in range(100):
        # 행의 sum 중 최대값
        sum_row = sum(arr[i])
        if max_arr < sum_row:
            max_arr = sum_row

        # 대각선 (오른쪽 아래로 내려가는) sum
        sum_rbottom += arr[i][i]
        # 대각선 (오른쪽 위로 올라가는) sum
        sum_rtop += arr[i][99-i]

        # 열의 sum 중 최대값
        sum_col = 0
        for j in range(100):
            sum_col += arr[j][i]
        if max_arr < sum_col :
            max_arr = sum_col

    if max_arr < sum_rtop :
        max_arr = sum_rtop
    if max_arr < sum_rbottom :
        max_arr = sum_rbottom
    print('#{} {}'.format(N, max_arr))
