import sys
input = sys.stdin.readline

n = int(input())
lst = [input().rstrip() for _ in range(n)]
lst.sort()
lst = sorted(lst, key =len)

temp = ''
for i in range(n):
    if temp != lst[i]:
        print(lst[i])
    temp = lst[i]
