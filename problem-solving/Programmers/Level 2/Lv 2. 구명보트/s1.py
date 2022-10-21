from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        temp = people.pop()
        if people :
            if limit-temp >= people[0] :
                people.popleft()
        answer += 1
    return answer