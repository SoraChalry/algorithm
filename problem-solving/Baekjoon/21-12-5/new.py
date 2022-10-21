import sys
input = sys.stdin.readline

delta = [(0,1),(1,0)]

def dfs(i, j):
    global result

    if visited[i][j]:
        return

    if board[i][j] == -1:
        result = True
        return

    if not result :
        step = board[i][j]

        for k in range(2):
            di, dj = delta[k][0]*step+i, delta[k][1]*step+j

            if 0<=di<n and 0<=dj<n and not visited[di][dj]:
                visited[di][dj] = 1
                # print(visited)
                dfs(di, dj)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
result = False
dfs(0,0)
if result :
    print('HaruHaru')
else :
    print('Hing')