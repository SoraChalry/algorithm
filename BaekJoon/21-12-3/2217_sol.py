n = int(input())
lst = list()
result = [ 0 for _ in range(n)]

for i in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
for j in range(n):
    result[j] = lst[j]*(j+1)
print(max(result))
