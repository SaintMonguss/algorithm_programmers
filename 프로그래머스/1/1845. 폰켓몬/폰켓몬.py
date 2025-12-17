def solution(nums):
    hashTable = []
    for i in nums:
        if not hash(i) in hashTable:
            hashTable.append(hash(i))
    return min(len(nums)/2, len(hashTable))
