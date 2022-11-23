#배열의 값을 두 배로 만들기 위해서 배열의 값들을 하나씩 꺼내서 2배로 만들고 answer에 넣으면 된다.
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer