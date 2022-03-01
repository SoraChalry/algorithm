import sys
'''
시간초과 발생 ㅠ
'''

n = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_pp = 9876543210
result = 0
for i in range(n):
    stay = lst[i][0]
    sum_pp = 0
    for j in range(n):
        sum_pp += lst[j][1]*abs(lst[j][0] - stay)
    if min_pp > sum_pp :
        min_pp = sum_pp
        result = stay

print(result)