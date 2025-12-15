def solution(n, works):
    works.sort(reverse = True)
    answer = 0
    while n > 0:
        MaxWork = works[0]
        for x in range(len(works)):
            if n > 0 and works[x] >= MaxWork:
                works[x] -= 1
                n -= 1
            elif n == 0 :
                break
    for i in works:
        if i > 0 :
            answer += i **2
    return answer