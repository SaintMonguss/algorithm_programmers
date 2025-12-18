from collections import deque

def solution(arr):
    q = deque()
    q.append(arr[0])
    for i in arr[1:]:
        if q[-1] != i:
            q.append(i)
    answer = list(q)
    
    return answer