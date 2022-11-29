#소수 빼고 출력
def solution(n):
    answer = 0
    num = 0
    for i in range(n+1):
        for j in range(n+1):
            if i>1 and j>1 and i>j and i%j==0:    
                answer+=1
                break
    return answer