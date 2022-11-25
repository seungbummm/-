#짝수 홀수는 %2가 0일때 짝수, 1일때 홀수
def solution(num_list):
    answer = [0,0]
    for i in num_list:
        if i%2 == 0:
            answer[0]+=1
        else:
            answer[1]+=1
            
    return answer