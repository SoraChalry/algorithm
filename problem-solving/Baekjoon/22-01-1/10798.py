import sys
input = sys.stdin.readline

s = [input().rstrip() for _ in range(5)]
max_length = 0
word = ''
for i in s:
    if len(i) > max_length:
        max_length = len(i)

for i in range(max_length):
    for j in range(5):
        if i<len(s[j]):
            word += s[j][i]
print(word)