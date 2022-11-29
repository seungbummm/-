def solution(my_string):
    answer = ''
    for i in my_string:
        b = i.isupper()
        if b == True:
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer