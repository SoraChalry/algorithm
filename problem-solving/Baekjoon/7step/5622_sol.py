numbers = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a = input()
count = 0
for i in a:
    for j in range(len(numbers)):
        if i in numbers[j]:
            count += j+3
print(count)