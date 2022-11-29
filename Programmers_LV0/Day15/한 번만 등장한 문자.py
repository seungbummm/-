def solution(s):
    answer = ''
    c = list()
    for i in s:
        if s.count(i)==1:
            c.append(i)
    answer = ''.join(sorted(c))
    return answer