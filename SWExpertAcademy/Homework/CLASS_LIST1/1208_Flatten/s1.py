import sys
sys.stdin = open('input.txt')
'''
    높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업 => 평탄화
    상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환
    [제약 사항]
        가로 길이는 항상 100
        모든 위치에서 상자의 높이는 1이상 100 이하
        덤프 횟수는 1이상 1000 이하
        주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행X 
        그 때의 최고점과 최저점의 높이 차를 반환(주어진 data에 따라 0 또는 1이 된다).
'''
for tc in range(1, 11):
    N = int(input())    # 덤프횟수
    box_height = list(map(int, input().split()))

    for i in range(N):
        box_height.sort()
        box_height[-1] -= 1
        box_height[0] += 1
    print('#{} {}'.format(tc, max(box_height)-min(box_height)))