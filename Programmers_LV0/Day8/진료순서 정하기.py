def solution(emergency):
    answer = []
    li = [0]*len(emergency)

    for i in emergency:
        for j in range(len(li)):
            if emergency[j] <= i:
                li[j] += 1
    answer = li
    return answer