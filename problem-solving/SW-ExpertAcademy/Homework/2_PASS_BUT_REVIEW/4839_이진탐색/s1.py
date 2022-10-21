import sys
sys.stdin = open('input.txt')
'''
    책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하라. 비긴 경우는 0을 출력
    [입력]
        첫 줄에 테스트 케이스 개수 T (1<=T<=50)
        테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000
'''
# def paging_search(P, A):
#     top = 0
#     bottom = P
#     count = 0
#     while True :
#         count += 1
#         middle = (top+bottom)//2
#         if middle == A :
#             return count
#         elif middle < A :
#             top = middle
#         else :
#             bottom = middle

def search(t, P, search_num):
    top = t
    bottom = P
    middle = (top+bottom)//2
    if middle == search_num :
        return 1
    elif middle < search_num :
        top = middle
    else :
        bottom = middle

    return search(top, bottom, search_num)+1


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    # A_count = paging_search(P, A)
    # B_count = paging_search(P, B)
    A_count = search(1, P, A)
    B_count = search(1, P, B)

    if A_count == B_count :
        print('#{} {}'.format(tc, 0))
    elif A_count < B_count :
        print('#{} {}'.format(tc, 'A'))
    else :
        print('#{} {}'.format(tc, 'B'))

