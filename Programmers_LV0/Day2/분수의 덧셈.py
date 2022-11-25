#분수의 덧셈은 분모에는 분모끼리 곱하고, 분자는 1번의 분자와 2번의 분모를 곱하고, 2번의 분자와 1번의 분모를 곱한 후 이를 더한다.
# math 함수에서 gcd(최대 공약수)를 이용하여 분자와 분모에 나눠준다.
import math
def solution(denum1, num1, denum2, num2):
    answer = []
    num = 0
    denum = 0
    denum = denum1*num2+num1*denum2
    num = num1*num2
    g = math.gcd(denum, num)
    answer.append(denum/g)
    answer.append(num/g)
    return answer