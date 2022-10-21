M,N = map(int, input().split())
'''
시간초과나서 찾아봄
참고 : https://deokkk9.tistory.com/17
해당 수의 제곱근까지만 검사해도 충분!!
'''
for i in range(M, N+1):
    if i > 1 :
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                break
        else:
            print(i)

