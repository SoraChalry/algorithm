N = int(input())

count = N//5
N1 = N%5
if N1%3 :
    for i in range(count,-1,-1):
        N2 = N - 5*i
        if N2%3 == 0:
            count = N2//3 + i
            break
    else :
        count = -1
else :
    count += N1//3

print(count)