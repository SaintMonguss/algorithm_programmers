def solution(participant, completion):
    starter = sorted(participant)
    finisher = sorted(completion)
    for x in range(len(finisher)):
        if starter[x] != finisher[x]:
            return starter[x]
    return starter[-1]