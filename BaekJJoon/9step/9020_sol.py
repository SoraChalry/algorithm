lst= []
for i in range(2, 10001):
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else :
        lst.append(i)

for _ in range(int(input())):
    n = int(input())
    result = []
    if n//2 in lst:
        print(n//2, n//2)
    else:
        for m in range(2, (n//2)):
            if m in lst:
                if (n-m) in lst:
                    result.append(m)
        print(result[-1], n-result[-1])
# for i in range(n):
#     a = int(input())
#     if prime(a // 2):
#         print(a // 2, a // 2)
#     else:
#         for j in range(2, (a // 2)):
#             if j in num:
#                 if (a - j) in num:
#                     list.append(j)
#         print(list[-1], a - list[-1])
#         list = []