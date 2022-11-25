#해당 문자열을 늘릴려면 인덱스 값에 복사하고싶은만큼 곱하면 된다.
def solution(my_string, n):
    answer = ''
    li = list(my_string)
    for i in li:
        answer += i*n
    
    return answer