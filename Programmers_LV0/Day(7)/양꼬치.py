def solution(n, k):
    answer = 0
    sheep = n*12000
    drink = k*2000
    service = (sheep//120000)*2000
    
    answer = sheep+drink-service
    return answer