def solution(numbers, k):
    answer = 0
    l = len(numbers)
    answer = ((k-1)*2)%l+1
    return answer