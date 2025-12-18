import math

def solution(progresses, speeds):
    
    dayList = [int(math.ceil((100-progresses[i]) / speeds[i])) for i in range(len(progresses))]
    answer = []
    n = 1
    long = dayList[0]
    for i in range(1, len(dayList)):
        if dayList[i] > long:
            answer.append(n)
            long = dayList[i]
            n = 1
        else:
            n += 1
    answer.append(n)

    return answer