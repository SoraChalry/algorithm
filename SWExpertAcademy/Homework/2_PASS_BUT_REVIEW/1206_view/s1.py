import sys
sys.stdin = open('input.txt')
'''

'''
for tc in range(1, 11):
    N = int(input())
    N_arr = list(map(int, input().split()))

    count = 0
    for i in range(2, N-2):
        sub_list = N_arr[i-2:i+3]
        base_len = sub_list[2]
        sub_list.remove(base_len)
        max_len = max(sub_list)
        if max_len >= base_len :
            continue
        count += base_len - max_len
    print('#{} {}'.format(tc, count))
