import sys
sys.stdin = open('sample2.txt')
'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''
T= int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    a = [input() for _ in range(N)]
    b = ['' for _ in range(N)]
    for k in a:
        for m in range(N):
            b[m] += k[m]

    for i in range(N):
        for j in range(N-M+1):
            if a[i][j:j+M] == a[i][j:j+M][::-1]:
                result = a[i][j:j+M]
            if b[i][j:j+M] == b[i][j:j+M][::-1]:
                result = b[i][j:j + M]
    print('#{} {}'.format(tc, result))