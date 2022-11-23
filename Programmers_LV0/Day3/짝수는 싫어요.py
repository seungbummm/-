#for 문에서 홀수만 출력할 수 있는데, 1부터시작해서 n+1까지 해주고, 하나 건너뛰고 출력하면 된다.
def solution(n):
    answer = []
    for i in range(1,n+1,2):
        answer.append(i)
    return answer