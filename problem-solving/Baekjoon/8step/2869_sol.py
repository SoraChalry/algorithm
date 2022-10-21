A,B,V = map(int, input().split())

result = (V-A)//(A-B) +1
if (V-A)%(A-B):
    result += 1

print(result)