def solution(n, times):
    times.sort()
    start = 0
    end = times[-1] * n
    answer = 0
    while start <= end:
        passCount = 0
        mid = (start + end) // 2
        for examiner in times:
            passCount += mid // examiner
            if n < passCount:
                break
        if n <= passCount:
            end = mid - 1
            answer = mid
        else :
            start = mid + 1
    return answer