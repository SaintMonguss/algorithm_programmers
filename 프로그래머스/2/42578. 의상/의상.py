from collections import defaultdict
from itertools import *

def init():
    return [None]

def solution(clothes):
    clothesType = defaultdict(init)
    for i in clothes:
        clothesType[i[1]].append(i[0])
    answer = 1
    for i in clothesType.values():
        answer *= len(i)
    return answer -1 