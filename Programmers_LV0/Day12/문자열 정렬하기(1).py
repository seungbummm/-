import re

def solution(my_string):
    answer = []
    n = re.findall('\d', my_string)
    n = sorted(n)
    answer = list(map(int, n))
    return answer