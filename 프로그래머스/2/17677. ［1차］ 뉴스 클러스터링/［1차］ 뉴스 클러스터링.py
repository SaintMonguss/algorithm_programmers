def solution(str1, str2):
    #조건에 맞춰서 리스트 생성
    list1= []
    for pos in range(len(str1) - 1):
        tmp = str1[pos:pos+2]
        if tmp.isascii() and tmp.isalpha():
            list1.append(tmp.upper())
    
    list2= []
    for pos in range(len(str2) - 1):
        tmp = str2[pos:pos+2]
        if tmp.isascii() and tmp.isalpha():
            list2.append(tmp.upper())

    size1 = len(list1)
    size2 = len(list2)
    # 공집합 예외처리
    if size1 == 0 and size2 == 0:
        return 65536
    if size1 == 0 or size2 == 0:
        return 0
    
    correctCount = 0
    if size1 <= size2:
        for x in list1:
            if x in list2:
                list2.remove(x)
                correctCount +=1
    else:
        for x in list2:
            if x in list1:
                list1.remove(x)
                correctCount +=1
                
    #검증
    print(list1)
    print(list2)
    print("size1 : " + str(size1))
    print("size2 : " + str(size2))
    print("correctCount : " + str(correctCount))
    print("answer : " + str(correctCount / (size1 + size2 - correctCount) *65536))
   
    return  0 if correctCount == 0 else int(correctCount / (size1 + size2 - correctCount) * 65536)