import sys
input = sys.stdin.readline

words = list(input().rstrip())
i = 0       # 현재 words의 위치
start = 0   #
while i < len(words):
    if words[i] == '<':
        i += 1
        while words[i] != '>':
            i += 1
        i += 1
    elif words[i].isalnum():
        start = i
        while i<len(words) and words[i].isalnum():
            i += 1
        temp = words[start:i]
        temp.reverse()
        words[start:i] = temp
    else:
        i+=1
print(''.join(words))
# for words in lst:
#     print(words[::-1], end=' ')

    # temp = words
    # len_num = len(temp)
    # for i in range(len_num-1, -1, -1):
    #     print(temp[i],end='')
    # print(end=' ')