N = int(input())
''' 
시간초과 ㅠㅠ
'''
# sol 1.
# for i in range(2, N+1):
#     for j in range(2, int(i**0.5)+1):
#         if i%j == 0:
#             break
#     else:
#         while N > 1:
#             if N % i:
#                 break
#             else:
#                 print(i)
#                 N //= i


# sol 2.
i = 2
while N > 1:
    if N % i == 0:
        print(i)
        N //= i
    else:
        i += 1