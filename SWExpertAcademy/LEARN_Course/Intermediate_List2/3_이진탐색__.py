import sys
sys.stdin = open('sample3.txt')

'''
 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.
            |            A            |           B
첫번째 탐색  |    l=1, r=400, c=200    |   l=1, r=400, c=200
두번째 탐색  |   l=200, r=400, c=300   |   l=1, r=200, c=100
세번째 탐색  |                         |   l=1, r=100, c=50
책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000
 
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.

'''
T = int(input())

def search(goal, left, right, count):
    c = int((left+right)/2)
    if c == goal:
        return count

    if c < goal:
        return search(goal, c, right, count+1)
    elif c > goal:
        return search(goal, left, c, count+1)

for tc in range(1, T+1):
    P,A,B = map(int, input().split())   # P: 페이지, A: A가 찾을 페이지, B: B가 찾을 페이지
    if search(A, 1, P, 0) == search(B, 1, P, 0):
        print(0)
    elif search(A, 1, P, 0) < search(B, 1, P, 0):
        print('A')
    else :
        print('B')