T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())
    lst = [w for w in range(n+1)]
    count = 0
    for i in range(k):
        for j in range(1, n+1):
            lst[j] += lst[j-1]
    print(lst[n])