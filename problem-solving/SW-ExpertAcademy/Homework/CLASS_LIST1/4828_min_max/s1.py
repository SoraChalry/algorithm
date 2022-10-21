import sys
sys.stdin = open('input.txt')
'''
    N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력
    [입력]
        첫 줄에 테스트 케이스의 수 T ( 1 ≤ T ≤ 50 )
        각 케이스의 첫 줄에 양수의 개수 N ( 5 ≤ N ≤ 1000 )
        다음 줄에 N개의 양수 ai ( 1 ≤ ai≤ 1000000 )
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai_list = list(map(int, input().split()))

    print('#{} {}'.format(tc, max(ai_list)-min(ai_list)))