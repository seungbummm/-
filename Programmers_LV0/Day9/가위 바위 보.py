def solution(rsp):
    answer = ''
    r = '0'
    s = '2'
    p = '5'
    a = list()
    rsp = list(rsp)
    for i in rsp:
        if i==r:
            a.append(p)
        elif i==s:
            a.append(r)
        else:
            a.append(s)
        answer = ''.join(a) 
    return answer