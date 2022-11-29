import re
def solution(my_string):
    answer = 0
    n = re.findall('\d', my_string)
    s = list(map(int, n))
    for i in s:
        answer += i
    return answer