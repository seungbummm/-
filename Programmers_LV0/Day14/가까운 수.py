def solution(order):
    answer = 0
    while order>0:
        n = order%10
        if n==0:
            n=10
        if n%3==0:
            answer+=1
        order//=10
    return answer