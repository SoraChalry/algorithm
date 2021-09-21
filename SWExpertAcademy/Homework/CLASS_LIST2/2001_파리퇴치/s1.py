import sys
sys.stdin = open('input.txt')
'''
    N x N 배열 안의 숫자는 파리의 개수
    M x M 크기의 파리채
    [제약 사항]
        1. N 은 5 이상 15 이하이다.
        2. M은 2 이상 N 이하이다.
        3. 각 영역의 파리 갯수는 30 이하 이다.
    [입력]
        가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
        각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
        다음 N 줄에 걸쳐 N x N 배열이 주어진다.
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_arr = list()

    for i in range(N-M+1):
        for j in range(N-M+1):
            sub_arr = list()
            for m in range(i, i+M):
                for n in range(j, j+M):
                    sub_arr.append(arr[m][n])
            sum_arr.append(sum(sub_arr))
    print('#{} {}'.format(tc, max(sum_arr)))