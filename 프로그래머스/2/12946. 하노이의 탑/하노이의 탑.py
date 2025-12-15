def solution(n):
    answer = []
    hanoi(n,1,2,3,answer)
    return answer

def hanoi(disk, start, sub, end, history):
    if disk == 1:
        history.append([start,end])
    else:
        hanoi(disk-1, start, end, sub, history)
        history.append([start,end])
        hanoi(disk-1, sub, start, end, history)
