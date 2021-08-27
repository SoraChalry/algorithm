import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(T) :
    N, M, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    N_list.sort()
    bread = 0
    result = 1

    for i in range(11112):
        if not result :
            break
        if i >= M and i%M == 0 :
            bread += K

        for j in N_list :
            if i == j :
                bread -= 1
                if bread >= 0 :
                    result = 1
                else :
                    result = 0
                    break
    if result :
        print('#{} {}'.format(idx+1, 'Possible'))
    else :
        print('#{} {}'.format(idx+1, 'Impossible'))

#   알고리즘 코딩의 법칙
#   지문을 읽는다
#   문제를 이해한다
#   손으로 풀어본다
#   풀이를 코딩한다
#   디버깅하고 검증한다
#
#오프더레코드
#



