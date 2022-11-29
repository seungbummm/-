def solution(numbers):
    answer = 0
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i, v in enumerate(num):
        numbers = numbers.replace(v,str(i))
    answer = int(numbers)
    return answer