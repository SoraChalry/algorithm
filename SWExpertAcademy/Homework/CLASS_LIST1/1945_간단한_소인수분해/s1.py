import sys
sys.stdin = open('input.txt')
'''
    N=2**a x 3**b x 5**c x 7**d x 11**e
    N이 주어질 때 a, b, c, d, e 를 출력
    [제약 사항]
        N은 2 이상 10,000,000 이하
    [입력]
        가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스
        각 테스트 케이스의 첫 번째 줄에 N  
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sosu = [2, 3, 5, 7, 11]
    sosu_alpha = [0]*5

    while N > 1 :
        for i in range(5) :
            if N % sosu[i]:
                continue
            N //= sosu[i]
            sosu_alpha[i] += 1

    print('#{}'.format(tc), *sosu_alpha)

