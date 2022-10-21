import sys
input = sys.stdin.readline

for tc in range(int(input())):
    words = input().strip()
    n = int(input())
    w_set = set(words)
    lst = list()
    min_w = 9876543210
    max_w = -1

    for i in w_set:
        if words.count(i) >= n:
            lst.append(i)

    for j in lst:
        pass
    # print(lst)
    if len(lst):
        print(min_w, max_w)
    else:
        print(-1)
