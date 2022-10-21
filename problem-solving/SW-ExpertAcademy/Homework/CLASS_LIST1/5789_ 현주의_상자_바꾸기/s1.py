import sys
sys.stdin = open('input.txt')
'''
    현주는 1번부터 N번까지 N개의 상자를 가지고 있다. 처음에는 모두 0
    Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경하려고 한다.
    i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
    현주가 Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을 순서대로 출력
    [입력]
        첫 번째 줄에 테스트 케이스의 수 T
        각 테스트 케이스의 첫 번째 줄에는 두 정수 N, Q (1 ≤ N, Q ≤ 103)가 공백으로 구분되어 주어진다.
        다음 Q개의 줄의 i번째 줄에는 Li, Ri (1 ≤ Li ≤ Ri ≤ N)이 주어진다.
'''
T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    N_box = [0]*N

    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            N_box[j] = i+1

    print('#{}'.format(tc), *N_box)