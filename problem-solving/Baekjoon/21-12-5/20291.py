import sys
input = sys.stdin.readline
t = int(input())
files = dict()
for _ in range(t):
    temp = ((input().split('.'))[1]).rstrip()
    if not temp in files:
        files[temp] = 1
    else:
        files[temp] += 1

result = sorted(files.items())

for key, val in result:
    print(key, val)
25