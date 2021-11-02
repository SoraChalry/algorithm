M,N = map(int, input().split())
'''
시간초과
'''
for i in range(M, N+1):
    for j in range(2, i):
        if i%j==0:
            break
    else:
        print(i)

