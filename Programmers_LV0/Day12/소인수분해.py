def solution(n):
    answer = []
    d = 2
    while n>1:
        if n%d == 0:
            n/=d
            answer.append(d)
            d=2
        else:
            d+=1
    answer = sorted(list(set(answer)))
    return answer