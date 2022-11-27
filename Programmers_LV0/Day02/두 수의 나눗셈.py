#10/3과 같은 경우 1000을 곱해도 소수로 표현된다. 그러므로 int형으로 고쳐서 소숫점을 없애주자
def solution(num1, num2):
    answer = int(num1/num2*1000)
    return answer