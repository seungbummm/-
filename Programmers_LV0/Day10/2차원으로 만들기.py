def solution(num_list, n):
    answer = [[]]
    l = len(num_list)
    nl = int(l/n)
    answer = list()
    for i in range(nl):
        a = list()
        for j in range(n*i, n*(i+1)):
            a.append(num_list[j])
            
        answer.append(list(a))
    
    return answer