
def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)      
    reserve_set = set(reserve) - set(lost)  

    for x in sorted(lost_set):
        if x - 1 in reserve_set:
            reserve_set.remove(x - 1)
        elif x + 1 in reserve_set:
            reserve_set.remove(x + 1)
        else:
            n -= 1
    return n