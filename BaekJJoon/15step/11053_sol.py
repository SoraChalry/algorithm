N = int(input())
lst = list(map(int, input().split()))
result = []
result.append(lst[0])

for i in lst[1:]:
    if i > result[-1]:
        result.append(i)

print(len(result))