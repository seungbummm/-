# 최빈값을 구하기 위해서 개수를 세서 풀어도 되지만, 각 숫자들을 한번 씩 지우는걸 반복하여 남는 값이 나오면 그 수가 최빈값이다. 없다면 개수가 같은거다.
def solution(array):
    while len(array)>0:
        for i, v in enumerate(set(array)):
            array.remove(v)
        if i==0:
            answer = v
        else:
            answer = -1
    return answer