import sys
sys.stdin = open('input.txt')
'''
    N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법
    ex) 10 1 9 2 8 3 7 4 6 5
    [입력]
        첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
        다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    new_arr = []

    for i in range(N):
        if i%2==0:
            max_num = arr.pop(-1)
            new_arr.append(max_num)
        else :
            min_num = arr.pop(0)
            new_arr.append(min_num)
    print('#{}'.format(tc), *new_arr[:10])
