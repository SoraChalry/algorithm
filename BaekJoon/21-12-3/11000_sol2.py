import heapq
import sys
'''
백준 시간초과 해결/ 입출력 속도 개선
https://breakcoding.tistory.com/109
heapq에 관한 설명 (시간복잡도 logN)
https://brownbears.tistory.com/550
'''
n = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lst.sort()                                  # 강의시간 리스트를 시작 시간을 기준으로 정렬

queue = []
heapq.heappush(queue, lst[0][1])            # 강의시간 리스트 중 첫 강의가 끝나는 시간을 queue에 배정

for i in range(1, n):
    # queue에 저장된 시간보다 다음 강의시간 시작 시간이 작은 경우
    if queue[0] > lst[i][0] :
        heapq.heappush(queue, lst[i][1])    # 강의가 끝나는 시간을 push해서 queue를 추가

    # queue에 저장된 시간과 다음 강의시간 시작 시간이 같거나 큰 경우
    else :
        heapq.heappop(queue)                # queue에 저장된 시간(최소값) pop으로 삭제
        heapq.heappush(queue, lst[i][1])    # 강의가 끝나는 시간을 새롭게 push해서 삭제된 queue자리에 갱신

print(len(queue))