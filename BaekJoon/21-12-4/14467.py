import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
lst = list(list(map(int, input().split())) for _ in range(n))

for i in range(n):
    number = -1
    for j in range(n):
        if i == lst[j][0]:
            if number != -1 and number != lst[j][1]:
                cnt +=1
            number = lst[j][1]

print(cnt)