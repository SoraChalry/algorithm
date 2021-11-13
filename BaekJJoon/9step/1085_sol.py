x,y,w,h = map(int, input().split())
check_lst = [0, 0, w, h]
min_length = 1000
for i in range(4) :
    temp = 0
    if i%2:
        temp = abs(y-check_lst[i])
    else :
        temp = abs(x-check_lst[i])
    if min_length > temp :
        min_length = temp

print(min_length)