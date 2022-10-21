import sys
sys.stdin = open('input.txt')

'''
    0에서 9까지 숫자가 적힌 N장의 카드
    가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력
    카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력
    [입력]
        첫 줄에 테스트 케이스 개수 T ( 1 ≤ T ≤ 50 )
        다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N ( 5 ≤ N ≤ 100 )
        다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pass