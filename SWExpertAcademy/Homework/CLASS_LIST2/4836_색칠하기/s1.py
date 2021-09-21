import sys
sys.stdin = open('input.txt')
'''
    N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램
    예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
    2
    2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
    3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )
    
    [입력]
        첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
        다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
        다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
        color = 1 (빨강), color = 2 (파랑)
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    paint_arr = [[0]*10 for _ in range(10)]
    count = 0

    for i in range(N):
        N_list = list(map(int, input().split()))
        color = N_list.pop(-1)
        st_r, st_c = map(int, N_list[0:2])
        end_r, end_c = map(int, N_list[2:4])

        for m in range(st_c, end_c+1):
            for n in range(st_r, end_r+1):
                paint_arr[m][n] += color

                if paint_arr[m][n] == 3 :
                    count +=1

    print('#{} {}'.format(tc, count))