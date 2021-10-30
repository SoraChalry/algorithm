A,B,C = map(int, input().split())
m = 1
while True :
    if A+B*m < C*m:
        break
    else :
        if C-B > 0:
            m = A//(C-B)+1
        else :
            m = -1
            break
print(m)