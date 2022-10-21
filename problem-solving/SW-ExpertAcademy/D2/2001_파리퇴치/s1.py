import sys
sys.stdin = open('input.txt')

'''
    N*N 배열 안의 숫자는 해당 영역에 존재하는 파리의 수
    M*M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
    [제약 사항]
        1. N 은 5 이상 15 이하이다.
        2. M은 2 이상 N 이하이다.
        3. 각 영역의 파리 갯수는 30 이하 이다.
    [입력]
        가장 첫줄은 테스트 케이스 개수 T
        각 테스트 케이스의 첫번째 줄에 N, M
        다음 N줄에 걸쳐 N*N 배열
'''
def fly_kill(r, c):
    sum_kill = 0
    for i in range(r, r+M):
        for j in range(c, c+M):
            sum_kill += N_arr[i][j]
    return sum_kill

T = int(input())
for idx in range(T) :
    N, M = map(int, input().split())
    N_arr = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0    # 파리를 죽인 최대값

    # M*M 크기의 파리채이므로 N*N 배열 안에서 파리채를 내리칠 수 있는 범위 : N-M+1
    for i in range(N-M+1):
        for j in range(N-M+1):

            #######################################################################
            # 1. for문을 통해 파리를 죽인 합을 구현
            # sum_kill = 0  # 파리를 죽인 합
            # M*M 크기의 파리채 범위
            # for m in range(i, M+i):
            #     for k in range(j, M+j):
            #         sum_kill += N_arr[m][k]     # 파리를 죽인 합을 구하는 계산
            #######################################################################

            # 2. 함수를 통해 파리를 죽인 합을 구현
            sum_kill = fly_kill(i,j)

            # 파리를 죽인 합이 최대값인지 비교
            if max_kill < sum_kill :
                max_kill = sum_kill
    # 출력
    print('#{} {}'.format(idx+1, max_kill))