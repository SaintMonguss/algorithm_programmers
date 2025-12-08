def solution(s):
    answer = [0,0]
    countNum1 = len(s) - s.count("0")
    while len(s) != 1:
        answer[0] += 1
        answer[1] += s.count("0")
        s = f"{countNum1:b}"
        countNum1 = len(s) - s.count("0")
    return answer