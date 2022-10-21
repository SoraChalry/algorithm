import sys
sys.stdin = open('input.txt')
'''
    N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
    M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력
    [입력]
        첫 줄에 테스트 케이스 개수 T ( 1 ≤ T ≤ 50 )
        다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
        다음 줄에 N개의 정수 ai ( 1 ≤ a ≤ 10000 )
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    ai_sum = list()
    for i in range(N-M+1):
        ai_sum.append(sum(ai[i:i+M]))

    print('#{} {}'.format(tc, max(ai_sum)-min(ai_sum)))