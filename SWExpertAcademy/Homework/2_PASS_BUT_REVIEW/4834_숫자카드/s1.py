import sys
sys.stdin = open('input.txt')

'''
    0에서 9까지 숫자가 적힌 N장의 카드
    가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력
    카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력
    [입력]
        첫 줄에 테스트 케이스 개수 T ( 1 ≤ T ≤ 50 )
        다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N ( 5 ≤ N ≤ 100 )
        다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 리스트에 입력된 모든 숫자를 하나씩 끊어서 넣어줌
    ai = list(map(int, input()))
    ai_count = [0]*10

    # 숫자카드를 갖고 있는 count 리스트
    for i in range(10) :
        ai_count[i] = ai.count(i)

    # 최대 count 구하기
    max_count = max(ai_count)
    max_index = 0

    for idx, val in enumerate(ai_count) :
        if val == max(ai_count):
            max_index = idx

    # 최대 count 수가 2개 이상인 경우, 가장 큰 index 구하기
    # if ai_count.count(max_count) > 1:
    #     for j in range(10) :
    #         if ai_count[j] == max_count :
    #             max_index = j
    # else :
    #     # 그 외
    #     max_index = ai_count.index(max(ai_count))

    print('#{} {} {}'.format(tc, max_index, max_count))