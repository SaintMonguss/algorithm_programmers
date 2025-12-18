def solution(sizes):
    long, short = sizes[0][0], sizes[0][1]
    if short > long:
        short, long = long, short
    for i in sizes[1:]:
        if i[0] >= i[1]:
            long = max(long, i[0])
            short = max(short, i[1])

        else :
            long = max(long, i[1])
            short = max(short, i[0])    

    answer = short * long
    return answer