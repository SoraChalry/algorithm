n = int(input())
lst = list(map(int, input().split()))
lst.sort()
for i in range(n):
    if i > 0:
        lst[i] = sum(lst[i-1:i+1])
print(sum(lst))