import sys
input = sys.stdin.readline

t = int(input())

'''
 45도 : 오른쪽으로 45도 회전
-45도 : 왼쪽으로 45도 회전
135도 : 오른쪽으로 45도 회전을 세번하기
'''
def turn_play(n, d, lst):
    idx = abs(d)//45
    flag = True
    if d < 0:
        flag = False

    for _ in range(idx):
        temp_lst = list()
        for i in range(n):  # 주대각선 임시 temp_lst에 담기
            temp_lst.append(lst[i][i])

        if flag:  # 양수이므로 시계방향
            for i in range(n):
                prev_temp = lst[i][n//2]
                lst[i][n//2] = temp_lst[i]
                temp_lst[i] = prev_temp
            for i in range(n):
                prev_temp = lst[i][n-1-i]
                lst[i][n-1-i] = temp_lst[i]
                temp_lst[i] = prev_temp
            for i in range(n):
                prev_temp = lst[n//2][n-1-i]
                lst[n//2][n-1-i] = temp_lst[i]
                temp_lst[i] = prev_temp
            for i in range(n):
                lst[n-1-i][n-1-i] = temp_lst[i]
        else:
            for i in range(n):
                prev_temp = lst[n // 2][i]
                lst[n // 2][i] = temp_lst[i]
                temp_lst[i] = prev_temp
            for i in range(n):
                prev_temp = lst[n - 1 - i][i]
                lst[n - 1 - i][i] = temp_lst[i]
                temp_lst[i] = prev_temp
            for i in range(n):
                prev_temp = lst[n - 1 - i][n // 2]
                lst[n - 1 - i][n // 2] = temp_lst[i]
                temp_lst[i] = prev_temp
            for i in range(n):
                lst[n - 1 - i][n - 1 - i] = temp_lst[i]

for _ in range(t):
    n, d = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    turn_play(n, d, lst)

    for i in range(n):
        for j in range(n):
            print(lst[i][j], end=' ')
        print()