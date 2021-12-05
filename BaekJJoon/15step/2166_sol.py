n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(1, n):
    result += lst[i-1][0]*lst[i][1] - lst[i-1][1]*lst[i][0]
result += (lst[n-1][0]*lst[0][1] - lst[n-1][1]*lst[0][0])
result = abs(result)*0.5

print(float(result))