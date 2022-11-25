def solution(age):
    answer = ''
    asc = 97
    c=''
    while age==0:
        n = age%10
        age //= 10
        c = chr(asc+n)+c
        
    answer = c
    return answer