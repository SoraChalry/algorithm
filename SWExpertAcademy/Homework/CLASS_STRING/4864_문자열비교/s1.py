import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    words = input()
    print('#{} {}'.format(tc, words.count(word)))