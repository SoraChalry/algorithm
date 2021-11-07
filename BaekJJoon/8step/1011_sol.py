for _ in range(int(input())):
    x,y = map(int, input().split())
    count = 0
    for i in range(x, y+1):
        if i == 0 :
            count +=1
        if i+2 < y+1:
            count +=1
    print(count)