import sys
sys.stdin = open('input.txt')
'''
[문제]
첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다.
이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?
[입력]
각 테스트 케이스의 첫 번째 줄에는 N (1 ≤ N ≤ 106)이 주어진다.

### 메모리사용:58,708kb, 실행시간:149ms, 코드길이:333
'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    sheep = set()
    result = 0
    i = 1
    while True :
        for j in str(i*N) :
            if not j in sheep:
                sheep.add(j)
        if len(sheep)==10:
            result = i*N
            break
        i += 1
    print('#{} {}'.format(tc, result))