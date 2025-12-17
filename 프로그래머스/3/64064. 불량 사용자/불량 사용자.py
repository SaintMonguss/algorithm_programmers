import re
from itertools import product

def solution(user_id, banned_id):
    maskWord = "[0-9a-z]"
    exceptList = []
    for ban in banned_id:
        tmpList = []
        for uid in user_id:
            replace = ban.replace("*", maskWord)
            matching = re.fullmatch(replace, uid)
            print("replace :" + replace +", uid :" + uid)
            if matching:
                tmpList.append(matching.group())
        if tmpList:
            exceptList.append(tmpList)
    
    tmp = set()    
    for i in product(*exceptList):
        tmp2 = frozenset(i)
        if len(tmp2) == len(banned_id):
            tmp.add(tmp2)
    return len(tmp)