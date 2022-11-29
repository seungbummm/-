def solution(n):
    answer = []
    c = 0
    while c<n:
        c += 1
        if n%c == 0:
            answer.append(c)
    return answer