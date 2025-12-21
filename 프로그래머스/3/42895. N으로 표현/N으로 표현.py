def solution(N, number):
    #dp를 하기 위해 들어온 n을 8번까지 사용하게 끔 배열을 셋팅
    dp = [set([int(str(N) * i)]) for i in range(1, 9)]
    
    #최대 8번 
    for i in range(8):
        # 이전에 한 연산들의 결과로 연산을 한다는게 핵심이라 가능한 연산 방식 n-1 회차를 하는게 골자
        for j in range(i):
            for num1 in dp[j]:
                for num2 in dp[i-j-1]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1//num2)
        if number in dp[i]:
            return i+1
    return -1