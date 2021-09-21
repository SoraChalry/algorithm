import sys
sys.stdin = open('input.txt')
'''
[문제]
1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
[제약사항]
N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

### 메모리사용:53,440kb, 실행시간:118ms, 코드길이:204
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0
    for i in range(1, N+1):
        if not i%2:
            i *= -1
        result += i
    print('#{} {}'.format(tc, result))