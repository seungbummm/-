def solution(s):
    answer = 0
    s = s.split(' ')
    a=list()
    for i in s:
        if i=='Z':
            a.pop()
        else:
            a.append(int(i))
    answer = sum(a)
    return answer