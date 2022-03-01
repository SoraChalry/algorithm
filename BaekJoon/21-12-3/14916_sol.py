money = int(input())
cnt = 0

if money:
    mok = money//5
    remain = money%5

    if mok and remain%2:
        cnt += mok-1
    else:
        cnt += mok
    money -= cnt*5

if money%2 :
    cnt = -1
else :
    cnt += money//2
print(cnt)