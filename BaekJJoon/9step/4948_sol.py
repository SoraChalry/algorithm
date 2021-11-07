'''
시간초과로 따로 소수 list를 만들어 놓고 시작하기
'''
lst = []
for i in range(2, 246912):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        lst.append(i)

while True:
    N = int(input())
    count = 0
    if N == 0:
        break
    else:
        for k in lst:
            if N < k <= 2*N:
                count += 1
    print(count)