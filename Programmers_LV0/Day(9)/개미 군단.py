def solution(hp):
    answer = 0
    g = hp//5
    hp = hp%5
    s = hp//3
    hp = hp%3
    w = hp
    answer = g+s+w
    
    return answer