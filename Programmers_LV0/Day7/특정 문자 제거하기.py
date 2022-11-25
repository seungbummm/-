def solution(my_string, letter):
    answer = ''
    li = my_string
    for i in li:
        if i != letter:
            answer+=i
    
    return answer