import sys
sys.stdin = open('sample3.txt')
'''


'''
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    lst = [0 for _ in range(len(str1))]
    for i in str2:
        for j in range(len(str1)):
            if i == str1[j]:
                lst[j] += 1
    print('#{} {}'.format(tc, max(lst)))