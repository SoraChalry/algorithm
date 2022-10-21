import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(T):
    N = int(input())
    arr = [input() for _ in range(N)]
    is_arr = []
    not_arr = []
    number = []
    count = 0
    for i in range(N):
        if arr[i].count('A') > 0:
            arr[i] = arr[i].replace('H','X')
            is_arr.append(i)
    for j in is_arr:
        arr[i]





    print(is_arr)
# 델타함수 잘 하기
# if, for문
#
#
#
#

#
#
#
#



