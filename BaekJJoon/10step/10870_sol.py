def pibo(N):
    if N == 0 :
        return 0
    elif N == 1 or N==2:
        return 1
    else :
        return pibo(N-1)+pibo(N-2)

n = int(input())
print(pibo(n))