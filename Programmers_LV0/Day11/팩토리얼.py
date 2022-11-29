def solution(n):
    answer = 0
    fac = 1
    while True:
        answer += 1
        fac *= answer
        if n/fac<answer:
            break

    return answer