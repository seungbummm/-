def solution(numbers, direction):
    answer = []
    if direction == "right":
        a = numbers[-1]
        del numbers[-1]
        numbers.insert(0,a)    
    else:
        a = numbers[0]
        del numbers[0]
        numbers.append(a)
    answer = numbers
    return answer