def solution(n):
    answer = 0
    num = 0
    cnt = 0
    for i in range(n):
        num+=1
        if n%num==0:
            cnt+=1
    answer = cnt
    return answer

