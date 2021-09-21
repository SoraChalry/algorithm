import sys
from builtins import print

sys.stdin = open('input.txt')
'''
    1부터 12까지의 숫자를 원소로 가진 집합 A
    집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수
    해당하는 부분집합이 없는 경우 0을 출력
    [입력]
        첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
        테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )
'''
T = int(input())
for tc in range(1, T+1):
    A = [a for a in range(1, 13)]
    N, K = map(int, input().split())
    count = 0
    m = 0
    for i in range(1<<len(A)):  # 총 부분집합이 만들어지는 경우의 수 2**N -1
        sub_list = []
        for j in range(len(A)): # 부분집합에 들어가는 조합 경우의 수
            if i & (1<<j):  # i=0, j=0 -> 1<<j = 1
                sub_list.append(A[j])
        if len(sub_list) == N :
            if sum(sub_list) == K :
                count += 1

    print('#{} {}'.format(tc, count))