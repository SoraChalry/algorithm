import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        f = q.popleft()
        if visited[f] == 0 :
            q.extendleft(r_lst[f])
            visited[f] = 1

n = int(input())
t = int(input())

# [] [2 5] [1 3 5] [2] [7] [1 2 6] [5] [4]
lst = [list(map(int, input().split())) for _ in range(t)]
r_lst = [[] for _ in range(n+1)]
visited = [0]*(n+1)
q = deque()

for i in range(1, n+1):
    for nums in lst:
        if i == nums[0]:
            r_lst[i].append(nums[1])
        elif i == nums[1]:
            r_lst[i].append(nums[0])

q.append(1)
bfs()
print(visited.count(1)-1)