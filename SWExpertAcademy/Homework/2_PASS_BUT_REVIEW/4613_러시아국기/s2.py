import sys
sys.stdin = open('input.txt')
t = int(input())

for tc in range(1, 1 + t):
    n, m = map(int, input().split())
    num_list = [list(input()) for _ in range(n)]
    wbr_cnt = []
    for i in range(n):
        wbr_cnt.append([num_list[i].count('W'), num_list[i].count('B'), num_list[i].count('R')])
    print(wbr_cnt)
    min_value = m * n
    for i in range(1, n - 1):
        for j in range(1, n - i):
            tmp = 0
            k = 0
            while k < n:
                if k < i:
                    tmp += m - wbr_cnt[k][0]
                elif k < i + j:
                    tmp += m - wbr_cnt[k][1]
                else:
                    tmp += m - wbr_cnt[k][2]
                k += 1
                if tmp > min_value:
                    break
            if tmp < min_value:
                min_value = tmp

    print('#{} {}'.format(tc, min_value))