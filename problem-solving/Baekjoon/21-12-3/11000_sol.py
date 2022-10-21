import sys
'''
시간초과 발생 ㅠ
'''

n = int(input())
lst = [list(map(int,  sys.stdin.readline().split())) for _ in range(n)]
lst.sort()          # 강의 시간 리스트를 정렬
new_lst = list()
cnt = 0             # 강의실 cnt

for sub in lst:     # 강의 시간 부분리스트 반복
    some = sub[1]   # 강의가 끝나는 시간
    if new_lst:
        for i in range(len(new_lst)) :
            if new_lst[i] <= sub[0]:
                cnt -= 1
                new_lst[i] = some
                break
            else :
                new_lst.append(some)
    else :
        new_lst.append(some) # 3 7
    cnt += 1

print(cnt)

# 1 3
# 2 7
# 3 5
