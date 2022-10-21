import sys
sys.stdin = open('input.txt')
'''
    주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력
    [제약 사항]
        N 은 5 이상 50 이하이다.
    [입력]
        가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
        각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print('#{}'.format(tc), *arr)