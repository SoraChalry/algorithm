import sys
sys.stdin = open('input.txt')
'''
[문제]
N=2**a x 3**b x 5**c x 7**d x 11**e
N이 주어질 때 a, b, c, d, e 를 출력하라.
[제약사항]
N은 2이상 10,000,000 이하

### 메모리사용:58,600kb, 실행시간:148ms, 코드길이:299
'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    taget = [2,3,5,7,11]
    result = [0,0,0,0,0]
    while N > 1:
        for i in range(len(taget)-1,-1,-1):
            if not N%taget[i]:
                N//=taget[i]
                result[i] +=1
    print('#{}'.format(tc), *result)