def solution(money):
    answer = []
    cup = money//5500
    M = money-cup*5500
    answer.append(cup)
    answer.append(M)
    return answer