N = int(input())
lst = list(map(int, input().split()))
count = 0
for i in range(N):
    if lst[i] > 1:
        for j in range(2, lst[i]):
            if lst[i] % j == 0:
                break
        else:
            count += 1
print(count)