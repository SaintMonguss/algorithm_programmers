from collections import defaultdict
import math

def solution(fees, records):
    defaultTime = fees[0]
    defaultCharge = fees[1]
    timeUnit = fees[2]
    unitCharge = fees[3]
    endTime = 23 * 60 + 59
    
    inHistory = {}
    outHistory = {}
    answer = []
    for x in range(len(records)):
        time, number, inOut = records[x].split(" ")
        hh, mm = time.split(":")
        minute = int(hh) * 60 + int(mm)
        if inOut == "IN":
            inHistory.setdefault(int(number), []).append(minute)
        else :
            outHistory.setdefault(int(number), []).append(minute)
    for car in inHistory:
        usingTime = 0
        charge = 0
        tmpOutHistory = outHistory.get(car)
        if not tmpOutHistory:
            outHistory.setdefault(car, []).append(endTime)
            tmpOutHistory = outHistory.get(car)
        elif len(inHistory[car]) > len(outHistory[car]): 
            outHistory[car].append(endTime)
        for num in range(len(inHistory[car])):
            usingTime += outHistory[car][num] - inHistory[car][num]
        charge = defaultCharge + math.ceil(max(0, usingTime - defaultTime) / timeUnit) * unitCharge
        
        answer.append([car, charge])
        answer.sort(key = lambda x: x[0])
    return [x[1] for x in answer]