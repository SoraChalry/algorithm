
while True:
    lst = list(map(int, input().split()))
    if lst.count(0)==3:
        break
    tall_num = max(lst)
    lst.remove(tall_num)
    num1, num2 = lst

    if num1**2+num2**2 == tall_num**2:
        print('right')
    else:
        print('wrong')