T = int(input())
count = 0
for tc in range(1, T+1):
    a = input()
    a_set = set()
    temp = ''
    for i in a:
        if temp != i :
            if i in a_set:
                break
            else :
                a_set.add(i)
        temp = i
    else :
        count +=1
print(count)